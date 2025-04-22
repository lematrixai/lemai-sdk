class UnsupportedProviderError(Exception):
    """Raised when an unsupported provider is specified."""
    pass

try:
    from .client import AIClient
except ImportError:
    AIClient = None

from .exceptions import UnsupportedProviderError  
