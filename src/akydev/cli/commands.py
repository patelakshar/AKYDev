from pathlib import Path

import typer
from rich.console import Console

from akydev.workspace.scanner import scan_workspace
from akydev.workspace.project_model import save_project_model
from akydev.workspace.task_manager import create_task
from akydev.planner.planner import generate_plan
from akydev.prompts.generator import generate_prompt
from akydev.providers.service import generate_response
from akydev.editor.validator import PatchValidator
from akydev.editor.apply import PatchApplier

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
def task(description: str = typer.Argument(...)):
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
            console.print(f" • #{task['id']}  {task['title']}  [{task['status']}]")

    console.rule("[bold green]Planner Ready")


@app.command()
def prompt():
    workspace = Path.cwd()

    prompt_file = generate_prompt(workspace)

    console.rule("[bold blue]Prompt Generated")
    console.print(prompt_file)
    console.rule("[bold green]Ready")


@app.command()
def implement():
    workspace = Path.cwd()

    response = generate_response(workspace)

    console.rule("[bold cyan]AI Response")
    console.print(response)
    console.rule("[bold green]Complete")


@app.command()
def review():
    workspace = Path.cwd()

    result = PatchValidator(workspace).validate()

    console.rule("[bold cyan]Patch Review")

    if result["valid"]:
        console.print("[bold green]✓ VALID[/bold green]")
    else:
        console.print("[bold red]✗ INVALID[/bold red]")

    console.print(result["reason"])

    console.rule("[bold green]Complete")

@app.command()
def apply():
    workspace = Path.cwd()

    validator = PatchValidator(workspace)

    result = validator.validate()

    if not result["valid"]:
        console.rule("[bold red]Patch Validation Failed")
        console.print(result["reason"])
        raise typer.Exit(1)

    result = PatchApplier(workspace).apply()

    console.rule("[bold cyan]Patch Apply")

    if result["success"]:
        console.print("[bold green]✓ SUCCESS[/bold green]")
    else:
        console.print("[bold red]✗ FAILED[/bold red]")

    console.print(result["reason"])

    console.rule("[bold green]Complete")


@app.command()
def commit():
    console.print("[yellow]Git automation coming soon...[/yellow]")
