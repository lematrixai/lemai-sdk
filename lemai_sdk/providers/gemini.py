import requests
from requests.exceptions import HTTPError
from .base import BaseProvider

class GeminiProvider(BaseProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    def chat(self, prompt: str):
        try:
            response = requests.post(
                self.base_url,
                json={"contents": [{"parts": [{"text": prompt}]}]}
            )
            response.raise_for_status()
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except HTTPError as e:
            if e.response.status_code == 400:
                return "Error: Invalid request format. Please check your prompt."
            elif e.response.status_code == 401:
                return "Error: Invalid API key. Please check your API key and try again."
            elif e.response.status_code == 403:
                return "Error: Access denied. Please check your API key permissions."
            elif e.response.status_code == 429:
                return "Error: Rate limit exceeded. Please try again later."
            else:
                return f"Error: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"