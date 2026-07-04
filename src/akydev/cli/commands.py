from pathlib import Path

import typer
from rich.console import Console

from akydev.workspace.scanner import scan_workspace

console = Console()


def analyze(path: str = typer.Argument(".")):
    """Analyze a project."""

    result = scan_workspace(Path(path))

    console.rule("[bold cyan]AKYDev Project Analyzer")

    for key, value in result.items():
        console.print(f"[green]{key:<12}[/green] : {value}")

    console.rule("[bold green]Analysis Complete")