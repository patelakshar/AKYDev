from pathlib import Path

import typer
from rich.console import Console

from akydev.workspace.scanner import scan_workspace

console = Console()


app = typer.Typer(help="AKYDev Commands")


@app.command()
def analyze(
    path: Path = typer.Argument(
        Path("."),
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
        help="Project directory to analyze.",
    ),
):
    """
    Analyze a software project.
    """

    result = scan_workspace(path)

    console.rule("[bold cyan]AKYDev Project Analyzer")

    for key, value in result.items():
        console.print(f"[green]{key:<18}[/green] : {value}")

    console.rule("[bold green]Analysis Complete")


@app.command()
def attach(
    path: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
        help="Project directory to attach.",
    ),
):
    """
    Attach a project workspace.
    """

    console.print(f"[bold green]✓ Attached project[/bold green]")
    console.print(path)


@app.command()
def task(
    description: str = typer.Argument(
        ...,
        help="Task description.",
    ),
):
    """
    Create a development task.
    """

    console.rule("[cyan]Task")
    console.print(description)


@app.command()
def review():
    """
    Review generated code.
    """

    console.print("[yellow]Review engine coming in Sprint 4...[/yellow]")


@app.command()
def apply():
    """
    Apply generated patch.
    """

    console.print("[yellow]Patch engine coming in Sprint 5...[/yellow]")


@app.command()
def commit():
    """
    Commit project changes.
    """

    console.print("[yellow]Git automation coming in Sprint 6...[/yellow]")