import os
from google.genai import types
def get_file_content(working_dir, file_path):

    MAX_CHARS = 10000

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
    print(file_content_string)
    return

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content.py",
    description="Reads file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
             "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path corresponding to the file we wish to run",
            ),
        },
    ),
)
