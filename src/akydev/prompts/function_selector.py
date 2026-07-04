import ast
from pathlib import Path


def extract_function(file: Path, name: str):

    tree = ast.parse(file.read_text())

    lines = file.read_text().splitlines()

    for node in tree.body:

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            if node.name == name:

                start = node.lineno - 1

                end = getattr(node, "end_lineno", start + 20)

                return "\n".join(lines[start:end])

    return None