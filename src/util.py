def get_system_prompt_from_file(filename: str) -> str:
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except IOError:
        return f"Error: Unable to read file '{filename}'."

