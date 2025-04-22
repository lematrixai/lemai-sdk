import os
import pytest

from lemai_sdk import AIClient

class DummyProvider:
    def chat(self, prompt):
        return f"Echo: {prompt}"

def test_ai_client_with_dummy():
    client = AIClient(provider="custom", api_key="fake", base_url="http://dummy")
    client.engine = DummyProvider()
    assert client.chat("hello") == "Echo: hello"