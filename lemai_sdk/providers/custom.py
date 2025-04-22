import requests
from requests.exceptions import HTTPError
from .base import BaseProvider

class CustomProvider(BaseProvider):
    def __init__(self, api_key: str, base_url: str):
        if not base_url:
            raise ValueError("Base URL required for custom provider")
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')  # Remove trailing slash if present

    def chat(self, prompt: str):
        try:
            # Format request based on the API endpoint
            if "deepseek" in self.base_url:
                response = requests.post(
                    f"{self.base_url}",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "deepseek-chat",
                        "messages": [{"role": "user", "content": prompt}]
                    }
                )
            else:
                # Default format for other APIs
                response = requests.post(
                    self.base_url,
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    json={"prompt": prompt}
                )
            
            response.raise_for_status()
            return response.json().get("response", "") or response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        except HTTPError as e:
            if e.response.status_code == 422:
                return "Error: Invalid request format. Please check the API documentation for the correct request format."
            elif e.response.status_code == 401:
                return "Error: Invalid API key. Please check your API key and try again."
            elif e.response.status_code == 404:
                return "Error: API endpoint not found. Please check the base URL."
            else:
                return f"Error: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"