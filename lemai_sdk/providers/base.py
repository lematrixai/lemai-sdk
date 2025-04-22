from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def chat(self, prompt: str):
        pass
