import json
from pathlib import Path


def generate_plan(workspace: Path) -> dict:
    project_file = workspace / ".akydev" / "project.json"
    tasks_dir = workspace / ".akydev" / "tasks"

    if not project_file.exists():
        raise FileNotFoundError("project.json not found. Run 'akydev analyze' first.")

    with project_file.open("r", encoding="utf-8") as f:
        project = json.load(f)

    tasks = []

    if tasks_dir.exists():
        for task in sorted(tasks_dir.glob("task-*.json")):
            with task.open("r", encoding="utf-8") as f:
                tasks.append(json.load(f))

    plan = {
        "project": project["Project"],
        "entry_point": project["Entry Point"],
        "python_files": project["Python Files"],
        "packages": project["Packages"],
        "pending_tasks": len(tasks),
        "tasks": tasks,
    }

    return plan
