import os
from google.genai import types

def write_file(working_dir, file_path, content):
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
    print(f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)")
    return 

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_dir": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path corresponding to the file we wish to run",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The file content to be read"
            ),
        },
    ),
)