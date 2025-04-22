from .providers.openai import OpenAIProvider
from .providers.gemini import GeminiProvider
from .providers.custom import CustomProvider
from .providers.config import get_api_key
from .exceptions import UnsupportedProviderError

class AIClient:
    SUPPORTED_PROVIDERS = ["openai", "gemini", "custom"]

    def __init__(self, provider: str, api_key: str = None, base_url: str = None):
        self.provider = provider.lower()
        self.api_key = api_key or get_api_key(self.provider)

        if self.provider == "openai":
            self.engine = OpenAIProvider(self.api_key)
        elif self.provider == "gemini":
            self.engine = GeminiProvider(self.api_key)
        elif self.provider == "custom":
            self.engine = CustomProvider(self.api_key, base_url)
        else:
            raise UnsupportedProviderError(
                f"Unsupported provider: {provider}. "
                f"Available providers are: {', '.join(self.SUPPORTED_PROVIDERS)} or use custom provider"
            )

    def chat(self, prompt: str):
        return self.engine.chat(prompt)