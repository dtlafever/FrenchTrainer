import chainlit as cl
from ollama import AsyncClient, ChatResponse, Client
import json
import time
# import anthropic
from decouple import config

from backend.llm.utils import get_system_prompt_from_file

from pathlib import Path

from mcp import ClientSession

# Use the ollama service name from docker-compose or fallback to localhost
OLLAMA_HOST = config("OLLAMA_HOST", "http://ollama:11434")
client = AsyncClient(host=OLLAMA_HOST)
sync_client = Client(host=OLLAMA_HOST)

# load environment variables
LLM_MODEL = config("LLM_MODEL", "phi4-mini")
SYSTEM_PROMPT = get_system_prompt_from_file(str(Path("data/system_prompts", config("SYSTEM_PROMPT_FILE"))))

async def ensure_model_exists(model_name=LLM_MODEL):
    """Check if model exists and pull it if it doesn't"""
    try:
        # List available models
        models = sync_client.list()
        available_models = [model['model'] for model in models.models]
        
        if model_name not in available_models:
            print(f"Model {model_name} not found. Pulling it now...")
            response = sync_client.pull(model_name)
            print(f"Successfully pulled model {model_name}")
        else:
            print(f"Model {model_name} is already available")
    except Exception as e:
        print(f"Error ensuring model exists: {e}")
        raise


@cl.on_chat_start
async def start_chat() -> None:
    """
    Set the system prompt and create a message history for our chat.
    Also initialize the database and tables if they don't exist.
    Ensure the LLM model is available, pulling it if needed.
    """
    # Make sure the model exists before we start the chat
    await ensure_model_exists()
    
    cl.user_session.set(
        "message_history",
        [
            {"role": "system", "content": SYSTEM_PROMPT},
        ]
    )

def flatten(xss):
    return [x for xs in xss for x in xs]

# async def call_claude(chat_messages):
#     msg = cl.Message(content="")
#     mcp_tools = cl.user_session.get("mcp_tools", {})
#     # Flatten the tools from all MCP connections
#     tools = flatten([tools for _, tools in mcp_tools.items()])
    
#     async with anthropic_client.messages.stream(
#         system=SYSTEM_PROMPT,
#         max_tokens=1024,
#         messages=chat_messages,
#         tools=tools,
#         model="claude-3-5-sonnet-20240620",
#     ) as stream:
#         async for text in stream.text_stream:
#             await msg.stream_token(text)
    
#     await msg.send()
#     response = await stream.get_final_message()

    # return response

async def call_ollama(message: cl.Message):
    # TODO: support for streaming
    message_history = cl.user_session.get("message_history")
    message_history.append({
        "role": "user",
        "content": message.content
    })

    # Ensure model exists before each chat
    await ensure_model_exists()

    mcp_tools = cl.user_session.get("mcp_tools", {})
    # Flatten the tools from all MCP connections
    tools = flatten([tools for _, tools in mcp_tools.items()])

    response: ChatResponse = sync_client.chat(
        model=LLM_MODEL,
        messages=message_history,
        tools=tools,
    )

    final_response = cl.Message(content="")

    if response.message.tool_calls:
        # There may be multiple tool calls in the response
        for tool in response.message.tool_calls:
            # Ensure the function is available, and then call it
            if function_to_call := tools.get(tool.function.name):
                print('Calling function:', tool.function.name)
                print('Arguments:', tool.function.arguments)
                output = function_to_call(**tool.function.arguments)
                print('Function output:', output)
            else:
                print('Function', tool.function.name, 'not found')

        # Only needed to chat with the model using the tool call results
        if response.message.tool_calls:
            # Add the function response to messages for the model to use
            message_history.append(response.message)
            message_history.append({'role': 'tool', 'content': str(output), 'name': tool.function.name})

            # Get final response from model with function outputs
            final_response = sync_client.chat(model=LLM_MODEL, messages=message_history)
            print('Final response:', final_response.message.content)

        else:
            print('No tool calls returned from model')

    if final_response.content != "":
        message_history.append({"role": "assistant", "content": final_response.content})
    await cl.Message(content=final_response.content).send()

async def get_streamed_response_from_llm(message: cl.Message) -> None:
    """
    Given a chainlit message, send the message to the LLM and stream the response
    to the UI. If the model supports "thinking", create a Step section for
    separating the thinking from the response to the user.

    Additionally, add the message sent from the user and the final response to
    the message_history stored in the cl.user_session.

    Args:
        message (cl.Message): the message object to send to LLM.
    Returns:
        None
    """
    start = time.time()
    message_history = cl.user_session.get("message_history")
    message_history.append({
        "role": "user",
        "content": message.content
    })
    
    # Ensure model exists before each chat
    await ensure_model_exists()

    # Get tools from all MCP connections
    mcp_tools = cl.user_session.get("mcp_tools", {})
    all_tools = [tool for connection_tools in mcp_tools.values() for tool in connection_tools]

    stream = await client.chat(
        model=LLM_MODEL,
        messages=message_history,
        tools=all_tools,
        stream=True
    )

    # The final answer from the LLM we want to add to display and add to the message history.
    final_answer = cl.Message(content="")

    # Stream response from the LLM. If there is thinking, stream that as a separate Step in the UI
    thinking = False
    async with cl.Step(name="Thinking") as thinking_step:

        async for chunk in stream:
            # delta = chunk.choices[0].delta
            delta = chunk.message

            if delta.content == "<think>":
                thinking = True
                continue

            if delta.content == "</think>":
                thinking = False
                thought_for = round(time.time() - start)
                thinking_step.name = f"Thought for {thought_for}s"
                await thinking_step.update()
                continue

            if thinking:
                await thinking_step.stream_token(delta.content)
            else:
                await final_answer.stream_token(delta.content)

    # Only add final answer to message history
    message_history.append({"role": "assistant", "content": final_answer.content})
    await final_answer.send()


@cl.on_message
async def on_user_message(message: cl.Message) -> None:
    """
    This is the callback function when a user message is received.
    When the user clicks submit, take that message in the text box as input into our LLM
    and return response from the Model.
    Called everytime a user inputs a message into the chatbot UI.

    Args:
        message (cl.Message): the message object the user sent when the user clicks submit.
    Returns:
        None
    """

    await call_ollama(message)
    # await get_streamed_response_from_llm(message)

@cl.step(type="tool") 
async def call_tool(tool_use):
    tool_name = tool_use.name
    tool_input = tool_use.input
    
    current_step = cl.context.current_step
    current_step.name = tool_name
    
    # Identify which mcp is used
    mcp_tools = cl.user_session.get("mcp_tools", {})
    mcp_name = None
    
    for connection_name, tools in mcp_tools.items():
        if any(tool.get("name") == tool_name for tool in tools):
            mcp_name = connection_name
            break
    
    if not mcp_name:
        current_step.output = json.dumps({"error": f"Tool {tool_name} not found in any MCP connection"})
        return current_step.output
    
    mcp_session, _ = cl.context.session.mcp_sessions.get(mcp_name)
    
    if not mcp_session:
        current_step.output = json.dumps({"error": f"MCP {mcp_name} not found in any MCP connection"})
        return current_step.output
    
    try:
        current_step.output = await mcp_session.call_tool(tool_name, tool_input)
    except Exception as e:
        current_step.output = json.dumps({"error": str(e)})
    
    return current_step.output

@cl.on_mcp_connect
async def on_mcp_connect(connection, session: ClientSession):
    """Called when an MCP connection is established"""
    # Your connection initialization code here
    # This handler is required for MCP to work
    
    # List available tools
    result = await session.list_tools()
    
    # Process tool metadata
    tools = [{
        "name": t.name,
        "description": t.description,
        "input_schema": t.inputSchema,
    } for t in result.tools]
    
    # Store tools for later use
    mcp_tools = cl.user_session.get("mcp_tools", {})
    mcp_tools[connection.name] = tools
    cl.user_session.set("mcp_tools", mcp_tools)

    print("MCP connection established.")

@cl.on_mcp_disconnect
async def on_mcp_disconnect(name: str, session: ClientSession):
    """Called when an MCP connection is terminated"""
    # Your cleanup code here
    # This handler is optional
    pass

    print("MCP connection terminated.")
