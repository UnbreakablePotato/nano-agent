import os
from google.genai import types

def write_file(working_dir, file_path, content):
    try:
        abs = os.path.abspath(working_dir)

        target_dir = os.path.normpath(os.path.join(abs,file_path))

        valid_target_dir = os.path.commonpath([abs, target_dir]) == abs

        existing_file = os.path.isfile(target_dir)

        is_dir = os.path.isdir(target_dir)

        if not valid_target_dir:
            print(f"Error: cannot write to \"{file_path}\" as it is outside the permitted working area")
            return
        
        if is_dir:
            print(f"Error: Cannot write to \"{file_path}\" as it is a directory")
            return
        
        os.makedirs(working_dir, exist_ok=True)

        with open(target_dir, "w") as f:
            f.write(content)
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: writing to file: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites content to a specific file path. If the file does not exist, it will be created.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The complete raw string (text or code) to be written into the file. This will replace any existing data."
            ),
        },
        required=["file_path", "content"],
    ),
)