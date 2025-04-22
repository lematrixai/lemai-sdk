import os

def get_api_key(provider: str):
    env_var = f"{provider.upper()}_API_KEY"
    return os.getenv(env_var)


### lemai_sdk/exceptions.py

class UnsupportedProviderError(Exception):
    pass