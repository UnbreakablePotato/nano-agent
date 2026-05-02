import os
from google.genai import types

def get_files_info(working_dir, directory="."):
    try:
        abs = os.path.abspath(working_dir)

        target_dir = os.path.normpath(os.path.join(abs,directory))

        valid_target_dir = os.path.commonpath([abs, target_dir]) == abs

        valid_dir = os.path.isdir(target_dir)

        items = os.listdir(target_dir)

        #for each item print "- {name}: file_size={bytes} bytes, is_dir={bool}"

        if not valid_target_dir:
            print(f'Error: Cannot list \"{directory}\" as it exists outside of the permitted working directory')
            return
        
        if not valid_dir:
            print(f'Error: the \" {directory}\" is not a directory')
            return
        files_info = []
        for item in items:
            full_item = os.path.join(target_dir, item)
            item_name = os.path.basename(item)
            item_size = os.path.getsize(full_item)
            item_dir = os.path.isdir(full_item)
            files_info.append(f"- {item_name}: file_size={item_size}, is_dir={item_dir}")
            return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
