from pathlib import Path

def get_system_prompt_from_file(filename: str) -> str:
    try:
        prompt_path = Path(f"prompts/{filename}")
        with open(prompt_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{prompt_path}' not found."
    except IOError:
        return f"Error: Unable to read file '{prompt_path}'."
