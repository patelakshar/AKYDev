from pathlib import Path

IGNORE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "dist",
    "build",
    ".idea",
    ".vscode",
}


def iter_python_files(root: Path):
    for path in root.rglob("*.py"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        yield path


def count_python_files(root: Path) -> int:
    return sum(1 for _ in iter_python_files(root))


def count_packages(src: Path) -> int:
    if not src.exists():
        return 0

    packages = set()

    for file in iter_python_files(src):
        if file.name == "__init__.py":
            packages.add(file.parent)

    return len(packages)


def detect_entry_point(root: Path):

    candidates = []

    for file in iter_python_files(root):

        if file.name in {
            "main.py",
            "__main__.py",
            "app.py",
            "cli.py",
        }:
            candidates.append(file)

    if candidates:
        return min(candidates, key=lambda p: len(p.parts)).relative_to(root).as_posix()

    return "Not Found"


def scan_workspace(root: Path):

    src = root / "src"

    return {
        "Project": root.name,
        "Git": (root / ".git").exists(),
        "README": (root / "README.md").exists(),
        "Tests": (root / "tests").exists(),
        "Python Project": (root / "pyproject.toml").exists(),
        "Source": src.exists(),
        "Python Files": count_python_files(root),
        "Packages": count_packages(src),
        "Entry Point": detect_entry_point(root),
    }