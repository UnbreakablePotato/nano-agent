import os
import subprocess
from google.genai import types

def run_python_file(working_dir, file_path:str, args=None):
    abs = os.path.abspath(working_dir)

    target_dir = os.path.normpath(os.path.join(abs,file_path))

    valid_target_dir = os.path.commonpath([abs, target_dir]) == abs

    existing_file = os.path.isfile(target_dir)

    if not valid_target_dir:
        print(f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working area")
        return
    
    if not existing_file:
        print(f"Error: \"{file_path}\" does not exist or is not a regular file")
        return
    
    if not file_path.endswith(".py"):
        print(f"\"{file_path}\" is not a Python file")
        return
    
    command = ["python", file_path]

    if args is not None:
        command.extend(args)

    completed_process = subprocess.run(command, cwd=abs,capture_output=True, text=True, timeout=30)

    if completed_process.returncode is None:
        print(f"Process exited with code {completed_process.returncode}")
        return
    
    if completed_process.stdout and completed_process.stderr is None:
        print("No output produced")
        return
    
    print(f"STDOUT: {completed_process.stdout}")
    print(f"STDERR: {completed_process.stderr}")
    return


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a python file with optional arguments. It can return error codes or string, otherwise it will print STDOUT or STDERR",
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
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="A list of tags",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="A single tag name"
                )
            ),
        },
    ),
)