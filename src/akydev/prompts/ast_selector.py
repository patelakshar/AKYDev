import ast
from pathlib import Path


def extract_symbols(file: Path) -> list[dict]:
    try:
        tree = ast.parse(file.read_text(encoding="utf-8"))
    except Exception:
        return []

    symbols = []

    for node in tree.body:

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            symbols.append(
                {
                    "type": "function",
                    "name": node.name,
                    "line": node.lineno,
                }
            )

        elif isinstance(node, ast.ClassDef):
            symbols.append(
                {
                    "type": "class",
                    "name": node.name,
                    "line": node.lineno,
                }
            )

    return symbols