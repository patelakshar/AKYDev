from pathlib import Path
import subprocess


class PatchApplier:

    def __init__(self, workspace: Path):
        self.workspace = workspace

    def apply(self) -> dict:

        patch = self.workspace / ".akydev" / "patch.diff"

        if not patch.exists():
            return {
                "success": False,
                "reason": "patch.diff not found",
            }

        result = subprocess.run(
            [
                "git",
                "apply",
                "--check",
                str(patch),
            ],
            cwd=self.workspace,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            return {
                "success": False,
                "reason": result.stderr.strip(),
            }

        result = subprocess.run(
            [
                "git",
                "apply",
                str(patch),
            ],
            cwd=self.workspace,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            return {
                "success": False,
                "reason": result.stderr.strip(),
            }

        return {
            "success": True,
            "reason": "Patch applied successfully.",
        }