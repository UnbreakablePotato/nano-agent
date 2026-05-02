import os
from google.genai import types
from nano.config import MAX_CHARS
def get_file_content(working_dir, file_path):

    try:
        abs = os.path.abspath(working_dir)

        target_dir = os.path.normpath(os.path.join(abs,file_path))

        valid_target_dir = os.path.commonpath([abs, target_dir]) == abs

        valid_file = os.path.isfile(target_dir)

        if not valid_target_dir:
            print(f"Error: cannot read \"{target_dir}\" as it is outside the permitted working directory")
            return
        
        if not valid_file:
            print(f"Error: File not found or is not a regular file: \"{target_dir}\"")
            return
        
        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(MAX_CHARS + 1) != "":
                file_content_string += f'[...File "{target_dir}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f"Error reading file \"{file_path}\": {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)