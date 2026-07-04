import typer

from akydev.cli.commands import (
    analyze,
    attach,
    apply,
    commit,
    review,
    task,
)

app = typer.Typer(
    name="akydev",
    help="AKYDev - AI Development Automation Platform",
    no_args_is_help=True,
)

app.command()(analyze)
app.command()(attach)
app.command()(task)
app.command()(review)
app.command()(apply)
app.command()(commit)

if __name__ == "__main__":
    app()