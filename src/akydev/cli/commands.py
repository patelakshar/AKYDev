from pathlib import Path

import typer
from rich.console import Console

from akydev.workspace.scanner import scan_workspace
from akydev.workspace.project_model import save_project_model
from akydev.workspace.task_manager import create_task
from akydev.planner.planner import generate_plan
from akydev.prompts.generator import generate_prompt

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
    ),
):
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
    ),
):
    console.print(f"[bold green]✓ Attached project[/bold green]")
    console.print(path)


@app.command()
def task(
    description: str = typer.Argument(...),
):
    workspace = Path.cwd()

    task_file = create_task(workspace, description)

    console.rule("[cyan]Task Created")
    console.print(f"[green]Title[/green] : {description}")
    console.print(f"[green]Saved[/green] : {task_file}")


@app.command()
def plan():
    workspace = Path.cwd()

    plan = generate_plan(workspace)

    console.rule("[bold magenta]Execution Plan")

    console.print(f"[green]Project[/green]        : {plan['project']}")
    console.print(f"[green]Entry Point[/green]    : {plan['entry_point']}")
    console.print(f"[green]Python Files[/green]   : {plan['python_files']}")
    console.print(f"[green]Packages[/green]       : {plan['packages']}")
    console.print(f"[green]Pending Tasks[/green]  : {plan['pending_tasks']}")

    if plan["tasks"]:
        console.print("\n[bold cyan]Tasks[/bold cyan]")

        for task in plan["tasks"]:
            console.print(
                f" • #{task['id']}  {task['title']}  [{task['status']}]"
            )

    console.rule("[bold green]Planner Ready")


@app.command()
def prompt():
    workspace = Path.cwd()

    prompt_file = generate_prompt(workspace)

    console.rule("[bold blue]Prompt Generated")
    console.print(prompt_file)
    console.rule("[bold green]Ready")


@app.command()
def review():
    console.print("[yellow]Review engine coming soon...[/yellow]")


@app.command()
def apply():
    console.print("[yellow]Patch engine coming soon...[/yellow]")


@app.command()
def commit():
    console.print("[yellow]Git automation coming soon...[/yellow]")
