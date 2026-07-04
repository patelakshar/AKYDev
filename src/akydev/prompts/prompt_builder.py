import json
from pathlib import Path


def build_prompt(workspace: Path) -> Path:
    project_file = workspace / ".akydev" / "project.json"
    tasks_dir = workspace / ".akydev" / "tasks"

    if not project_file.exists():
        raise FileNotFoundError("project.json not found")

    with project_file.open("r", encoding="utf-8") as f:
        project = json.load(f)

    tasks = []

    if tasks_dir.exists():
        for task_file in sorted(tasks_dir.glob("task-*.json")):
            with task_file.open("r", encoding="utf-8") as f:
                tasks.append(json.load(f))

    lines = []

    lines.append("# AKYDev Prompt")
    lines.append("")
    lines.append("## Project")
    lines.append(f"Name: {project['Project']}")
    lines.append(f"Entry Point: {project['Entry Point']}")
    lines.append(f"Python Files: {project['Python Files']}")
    lines.append(f"Packages: {project['Packages']}")
    lines.append("")

    lines.append("## Tasks")

    for task in tasks:
        lines.append(f"- [{task['status']}] {task['title']}")

    lines.append("")
    lines.append("## Instructions")
    lines.append("Implement ONLY the pending tasks.")
    lines.append("Maintain existing architecture.")
    lines.append("Do not rename files.")
    lines.append("Generate production-ready Python code.")
    lines.append("Return unified diff patches only.")

    prompt = "\n".join(lines)

    output = workspace / ".akydev" / "prompt.txt"

    output.write_text(prompt, encoding="utf-8")

    return output
