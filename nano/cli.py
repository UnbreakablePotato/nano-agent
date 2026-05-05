import typer
from nano.main import generate_content

app = typer.Typer()

def parse(content:str, model:str = ""):
    user_input = typer.prompt("$")


def begin_chat():
    while True:
        user_input = typer.prompt("$")

        input = user_input.lower()

        if input in ["Goodbye"]:
            typer.echo("Call me anytime you need!")
            raise typer.Exit()
        
        generate_content(input)




if __name__ == "__main__":
    app()