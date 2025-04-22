# LemAI SDK

A simple and flexible Python SDK for working with multiple AI providers like OpenAI, Gemini, or any custom LLM.

## Installation

```bash
pip install lemai-sdk
```

## Usage

```python
from lemai_sdk import AIClient

client = AIClient(provider="openai", api_key="your_openai_key")
response = client.chat("Tell me a joke")
print(response)
```

You can also use `GEMINI_API_KEY`, `OPENAI_API_KEY`, etc., in your environment variables.

For custom

```python
from lemai_sdk import AIClient

client = AIClient(
    provider="custom",
    api_key="your_custom_key_here",
    base_url="http://your-custom-llm.com/api/chat"
)
response = client.chat("What's the weather like today?")
print(response)
```

## Supported Providers
- OpenAI
- Gemini
- Custom (pass your own `base_url` and API key)