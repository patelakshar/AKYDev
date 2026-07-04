import json
from pathlib import Path

from akydev.prompts.context_builder import collect_source_code


def build_prompt(workspace: Path) -> Path:
    project = json.loads(
        (workspace / ".akydev" / "project.json").read_text()
    )

    tasks = []

    tasks_dir = workspace / ".akydev" / "tasks"

    if tasks_dir.exists():
        for task in sorted(tasks_dir.glob("task-*.json")):
            tasks.append(json.loads(task.read_text()))

    context = collect_source_code(workspace, tasks[0]["title"] if tasks else "")

    prompt = f"""
You are a Senior Python Software Engineer.

========================
PROJECT
========================

Name: {project["Project"]}

Entry Point: {project["Entry Point"]}

Python Files: {project["Python Files"]}

Packages: {project["Packages"]}

========================
TASKS
========================

"""

    for task in tasks:
        prompt += f"""
Task #{task["id"]}

Title: {task["title"]}

Status: {task["status"]}

"""

    prompt += """

========================
SOURCE CODE
========================

"""

    prompt += context

    prompt += """

========================
RULES
========================

- Keep existing architecture.
- Modify only required files.
- Produce production-quality code.
- Return ONLY a unified diff patch.
- Do not explain your answer.
"""

    output = workspace / ".akydev" / "prompt.txt"

    output.write_text(prompt, encoding="utf-8")

    return output
