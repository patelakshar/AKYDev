from pathlib import Path

import typer
from rich.console import Console

from akydev.workspace.scanner import scan_workspace
from akydev.workspace.project_model import save_project_model

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

    save_path = save_project_model(result, path)

    console.rule("[bold cyan]AKYDev Project Analyzer")

    for key, value in result.items():
        console.print(f"[green]{key:<18}[/green] : {value}")

    console.print()

    console.print(f"[bold blue]Project Model[/bold blue] : {save_path}")

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
    console.print(f"[bold green]✓ Attached project[/bold green]")
    console.print(path)


@app.command()
def task(
    description: str = typer.Argument(...),
):
    """
    Create a new task.
    """

    workspace = Path.cwd()

    from akydev.workspace.task_manager import create_task

    task_file = create_task(workspace, description)

    console.rule("[cyan]Task Created")
    console.print(f"[green]Title[/green] : {description}")
    console.print(f"[green]Saved[/green] : {task_file}")


@app.command()
def review():
    console.print("[yellow]Review engine coming in Sprint 4...[/yellow]")


@app.command()
def apply():
    console.print("[yellow]Patch engine coming in Sprint 5...[/yellow]")


@app.command()
def commit():
    console.print("[yellow]Git automation coming in Sprint 6...[/yellow]")