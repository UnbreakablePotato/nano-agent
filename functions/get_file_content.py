import os
def get_file_content(working_dir, file_path):

    MAX_CHARS = 10000

    abs = os.path.abspath(working_dir)

    target_dir = os.path.normpath(os.path.join(abs,file_path))

    full_path = os.path.join(target_dir,file_path)

    valid_target_dir = os.path.commonpath([abs, target_dir]) == abs

    if not valid_target_dir:
        print(f"Error: cannot read \"{file_path}\" as it is outside the permitted working directory")
        return
    
    if not os.path.isfile(full_path):
        print(f"Error: File not found or is not a regular file: \"{file_path}\"")
        return
    #
    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if f.read(MAX_CHARS + 1) is not None:
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

