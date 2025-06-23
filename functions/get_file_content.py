import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        base_dir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(base_dir, file_path))

        if not target_file.startswith(base_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, 'r', encoding='utf-8') as file:
            content = file.read()
            if len(content) > 10000:
                content = content[:1000] + f'\n [...File "{file_path}" truncated at 10000 characters]'
            return content

    except Exception as e:
        return f'Error: {e}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)