import json
from pathlib import Path


def save_project_model(project_data: dict, workspace: Path) -> Path:
    """
    Save the project model to .akydev/project.json
    """

    akydev_dir = workspace / ".akydev"
    akydev_dir.mkdir(parents=True, exist_ok=True)

    output = akydev_dir / "project.json"

    with output.open("w", encoding="utf-8") as f:
        json.dump(project_data, f, indent=4)

    return output