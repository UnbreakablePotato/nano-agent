import os
from google.genai import types

def get_cwd(working_dir):
    cwd = os.getcwd()

    return f"The current working directory is \"{cwd}\""

schema_get_cwd = types.FunctionDeclaration(
    name="get_cwd",
    description="Return the current working directory",
)