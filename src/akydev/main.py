import typer

from akydev.cli.commands import analyze

app = typer.Typer(
    name="akydev",
    help="AI Development Automation Platform",
)

app.command("analyze")(analyze)


if __name__ == "__main__":
    app()