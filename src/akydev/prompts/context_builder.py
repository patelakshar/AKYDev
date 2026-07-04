from pathlib import Path
import re

from akydev.prompts.ast_selector import extract_symbols
from akydev.prompts.function_selector import extract_function

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "tests",
    "test",
    "docs",
    "examples",
    "tutorials",
    "notebooks",
    "fundamentals",
    "training",
}

KEYWORDS = {
    "http": ["http", "request", "api", "client"],
    "probe": ["probe", "scan", "fingerprint"],
    "dns": ["dns", "resolver"],
    "port": ["port", "socket"],
    "report": ["report"],
}


def extract_keywords(task: str) -> set[str]:
    words = set(re.findall(r"[A-Za-z_]+", task.lower()))

    expanded = set(words)

    for word in list(words):
        expanded.update(KEYWORDS.get(word, []))

    return expanded


def score_file(path: Path, keywords: set[str]) -> int:
    score = 0

    filename = path.as_posix().lower()

    for keyword in keywords:
        if keyword in filename:
            score += 100

    if filename.endswith("main.py"):
        score += 25

    return score


def collect_source_code(
    workspace: Path,
    task: str,
    max_files: int = 3,
) -> str:

    src = workspace / "src"

    if not src.exists():
        return ""

    keywords = extract_keywords(task)

    candidates = []

    for file in src.rglob("*.py"):

        if any(part in IGNORE_DIRS for part in file.parts):
            continue

        score = score_file(file, keywords)

        if score == 0:
            continue

        candidates.append((score, file))

    candidates.sort(key=lambda item: item[0], reverse=True)

    sections = []

    for _, file in candidates[:max_files]:

        try:
            symbols = extract_symbols(file)

            snippet = file.read_text(encoding="utf-8")

            if symbols:
                extracted = extract_function(file, symbols[0]["name"])
                if extracted:
                    snippet = extracted

            names = ", ".join(s["name"] for s in symbols[:10]) if symbols else "None"

            section = (
                f"### FILE: {file.relative_to(workspace)}\n\n"
                f"Functions/Classes: {names}\n\n"
                "```python\n"
                f"{snippet}\n"
                "```\n"
            )

            sections.append(section)

        except Exception:
            continue

    return "\n\n".join(sections)