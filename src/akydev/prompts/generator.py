from pathlib import Path

from akydev.prompts.prompt_builder import build_prompt


def generate_prompt(workspace: Path) -> Path:
    """
    Generate the AI prompt for the current workspace.
    """
    return build_prompt(workspace)
