from akydev.providers.base import AIProvider


class MockProvider(AIProvider):
    """
    Temporary provider until Gemini/OpenAI/Ollama are added.
    """

    def generate(self, prompt: str) -> str:
        return f"""# AKYDev Mock Response

Prompt received successfully.

Characters: {len(prompt)}

Next Sprint:
- Connect Gemini
- Send prompt
- Receive response
- Save response
"""
