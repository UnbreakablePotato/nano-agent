import typer
from rich import print
from nano.main import generate_content
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

current_file = Path(__file__).resolve()

env_path = current_file.parent.parent / ".env"

app = typer.Typer(help="Nano Agent: Your local AI agent!")


def begin_chat(selected_model: str = ""):
    while True:
        user_input = typer.prompt("$")

        input:str = user_input.lower()

        if input in ["goodbye"]:
            typer.echo("Call me anytime you need!")
            raise typer.Exit()

        if input.startswith("/"):
            input_list = input.rsplit("/")
            file_name = input_list[1]
            """
            string will look like /skill

            input = create_skill(skill_dir, file_name+".md")

            generate_content(input, model_arg=selected_model)
            """


        generate_content(input, model_arg=selected_model)


@app.command()
def set_model(
    model: str = typer.Option("gemini-2.5-flash", "--model", "-m")
):
    
    """
    Sets the model of your choice. Make sure you have the correct api key setup for your model
    """
    begin_chat(selected_model=model)

@app.command("--api_key")
def set_api(
    api_key:str = typer.Option("", "--api_key", prompt=True, hide_input=True, help="Set your API key for a current model. \n Note! If you change to a different provider, you have to set your api key again...")
):  
    """
    Set your API key for a current model. \n Note! If you change to a different provider, you have to set your api key for that specific provider e.g. Anthropic, Google or openAI
    """
    try:
        with open(env_path, "w") as f:
            f.write(f"\nGEMINI_API_KEY={api_key}")
    except Exception as e:
        print(f"Error while attempting to open file: {e}")

@app.command("--create_skill")
def create_skill(name:str, content:str):
    """
    Creates a skill with a name and skill content
    """
    try:
        path = os.environ.get("skill_path")

        file_name = name + ".md"

        if not path:
            print(f"Error: path \"{path}\" is not a valid path")

        target_dir = os.path.normpath(os.path.join(path,file_name))

        print(target_dir)
        
        with open(target_dir, "w") as f:
            f.write(f"{name}\n")
            f.write(f"{content}")
    except Exception as e:
        print(f"Error while creating skill: {e}")


if __name__ == "__main__":
    app()