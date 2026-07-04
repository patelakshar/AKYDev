import ast
from pathlib import Path


def find_imports(file: Path) -> list[str]:
    """
    Extract imported module names from a Python file.
    """

    try:
        tree = ast.parse(file.read_text(encoding="utf-8"))
    except Exception:
        return []

    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    return sorted(set(imports))


def build_dependency_graph(workspace: Path) -> dict:

    src = workspace / "src"

    graph = {}

    if not src.exists():
        return graph

    for file in src.rglob("*.py"):

        graph[str(file.relative_to(workspace))] = find_imports(file)

    return graph
