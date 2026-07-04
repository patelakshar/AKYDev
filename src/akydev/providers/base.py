from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Base class for every AI provider.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
