import json
from datetime import datetime
from pathlib import Path


def create_task(workspace: Path, title: str) -> Path:
    tasks_dir = workspace / ".akydev" / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)

    existing = sorted(tasks_dir.glob("task-*.json"))
    task_id = len(existing) + 1

    task = {
        "id": task_id,
        "title": title,
        "status": "pending",
        "priority": "normal",
        "created": datetime.now().isoformat(timespec="seconds"),
        "workspace": workspace.name,
    }

    output = tasks_dir / f"task-{task_id:04}.json"

    with output.open("w", encoding="utf-8") as f:
        json.dump(task, f, indent=4)

    return output
