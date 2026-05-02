import os 
from google.genai import types

def create_dir(working_dir, dir_name):
    try:
        abs = os.path.abspath(working_dir)

        full_path = os.path.join(abs,dir_name)

        os.makedirs(full_path, exist_ok=False)
    except Exception as e:
        return f"Error creating directory: {e}"


schema_create_dir = types.FunctionDeclaration(
    name="create_dir",
    description="Creates a directory within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "dir_name": types.Schema(
                type=types.Type.STRING,
                description="name of the directory to create",
            ),
        },
    ),
)