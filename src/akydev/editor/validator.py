from pathlib import Path
import re


class PatchValidator:

    def __init__(self, workspace: Path):
        self.workspace = workspace

    def validate(self) -> dict:

        patch = self.workspace / ".akydev" / "patch.diff"

        if not patch.exists():
            return {
                "valid": False,
                "reason": "patch.diff not found",
            }

        text = patch.read_text(encoding="utf-8")

        if not text.startswith("diff --git"):
            return {
                "valid": False,
                "reason": "Not a unified diff",
            }

        files = re.findall(r"diff --git a/(.*?) b/", text)

        missing = []

        for file in files:

            target = self.workspace / file

            if not target.exists():

                if "new file mode" not in text:
                    missing.append(file)

        if missing:

            return {
                "valid": False,
                "reason": f"Missing files: {', '.join(missing)}",
            }

        return {
            "valid": True,
            "reason": "Patch looks valid",
        }