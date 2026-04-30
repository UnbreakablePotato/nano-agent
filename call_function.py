from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.create_directory import create_dir, schema_create_dir

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
        schema_create_dir
    ]
)

function_map = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "write_file": write_file,
    "run_python_file": run_python_file,
    "create_dir": create_dir
    }

def call_function(function_call, verbose=False):
    if verbose is True:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    func_name = function_call.name or ""

    if func_name not in function_map:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=func_name,
            response={"error": f"Unknown function: {func_name}"},
        )
    ],
)
    args = dict(function_call.args) if function_call.args else {}

    #To change the default working directory, change the string below
    args["working_dir"] = "./calculator"

    func_res = function_map[func_name](**args)

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=func_name,
            response={"result": func_res},
        )
    ],
)

    