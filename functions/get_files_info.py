import os

def get_files_info(working_dir, directory="."):
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
    
    for item in items:
        full_item = os.path.join(target_dir, item)
        item_name = os.path.basename(item)
        item_size = os.path.getsize(full_item)
        item_dir = os.path.isdir(full_item)

        print(f"- {item_name}: file_size={item_size}, is_dir={item_dir}")


