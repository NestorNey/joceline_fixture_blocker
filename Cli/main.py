import typer
from Utils.loadConfig import loadConfig

loadConfig()

app = typer.Typer()

@app.command()
def savetestinfo():
    print("Something...")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

if __name__ == "__main__":
    app()