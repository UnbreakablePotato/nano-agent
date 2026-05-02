import os
import subprocess
from google.genai import types
import json

def run_python_file(working_dir, file_path:str, args=None):
    try:
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
        output = []
        if completed_process.returncode is None:
            output.append(f"Process exited with code {completed_process.returncode}")
            
        
        if completed_process.stdout and completed_process.stderr is None:
            output.append("No output produced")
            
        
        if completed_process.stdout:
            output.append(f"STDOUT: {completed_process.stdout}")
       
        if completed_process.stderr:
            output.append(f"STDERR: {completed_process.stderr}")
        return "\n".join(output)
    
    except Exception as e:
        return f"Error while executing python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    ),
)

openAI_run_python_file = [
  {
    "type": "function",
    "function": {
      "name": "run_python_file",
      "description": "Executes a specified Python file within the working directory and returns its output",
      "parameters": {
        "type": "object",
        "properties": {
          "file_path": {
            "type": "string",
            "description": "Path to the Python file to run, relative to the working directory"
          },
          "args": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Optional list of arguments to pass to the Python script"
          }
        },
        "required": ["file_path"],
        "additionalProperties": False
      }
    }
  }
]