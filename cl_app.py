import chainlit as cl
from ollama import AsyncClient
import time
from decouple import config

from src.util import get_system_prompt_from_file

from pathlib import Path

client = AsyncClient()

# load environment variables
LLM_MODEL = config("LLM_MODEL")
SYSTEM_PROMPT = get_system_prompt_from_file(str(Path("data/system_prompts", config("SYSTEM_PROMPT_FILE"))))


@cl.on_chat_start
def start_chat() -> None:
    """
    Set the system prompt and create a message history for our chat.
    Also initialize the database and tables if they don't exist.
    """
    cl.user_session.set(
        "message_history",
        [
            {"role": "system", "content": SYSTEM_PROMPT},
        ]
    )

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

    stream = await client.chat(
        messages=message_history,
        model=LLM_MODEL,
        stream=True,
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

    await get_streamed_response_from_llm(message)


