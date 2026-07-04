import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


SYSTEM_PROMPT = """
You are AKYDev.

You are an expert Python software engineer.

Rules:

- Return ONLY a unified git diff.
- Do NOT explain anything.
- Do NOT wrap the answer in markdown.
- Do NOT write prose.
- Do NOT invent filenames.
- Modify only existing files unless absolutely required.
- Output must start with:

diff --git
"""


def generate_response(workspace: Path) -> Path:

    project_root = Path(__file__).resolve().parents[3]

    load_dotenv(project_root / ".env")

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY")

    prompt_file = workspace / ".akydev" / "prompt.txt"

    if not prompt_file.exists():
        raise RuntimeError("prompt.txt not found")

    prompt = prompt_file.read_text(encoding="utf-8")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\n{prompt}",
    )

    patch = response.text.strip()

    output = workspace / ".akydev" / "patch.diff"

    output.write_text(patch, encoding="utf-8")

    return output