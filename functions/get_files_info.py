import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    try:
        base_dir = os.path.abspath(working_directory)
        target_dir = os.path.abspath(os.path.join(base_dir, directory or ""))

        if not target_dir.startswith(base_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        lines = []
        for entry in os.listdir(target_dir):
            entry_path = os.path.join(target_dir, entry)
            try:
                size = os.path.getsize(entry_path)
                is_dir = os.path.isdir(entry_path)
                lines.append(f'- {entry}: file_size={size} bytes, is_dir={is_dir}')
            except Exception as e:
                return f'Error: Failed to read entry "{entry}": {e}'

        return "\n".join(lines)

    except Exception as e:
        return f'Error: {e}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)