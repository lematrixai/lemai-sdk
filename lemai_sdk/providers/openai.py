from openai import OpenAI
from openai import RateLimitError
from .base import BaseProvider

class OpenAIProvider(BaseProvider):
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def chat(self, prompt: str):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except RateLimitError:
            return "I apologize, but I'm currently experiencing high demand. You exceeded your current quota, please check your plan and billing details or check your OpenAI account quota."
        except Exception as e:
            return f"An error occurred: {str(e)}"