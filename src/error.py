class ApiError(Exception):
    """Exception base class for api-related errors."""

class UnexpectedApiError(ApiError):
    """Raised when the API returned an unexpected response."""
    
    def __init__(self, response) -> None:
        super().__init__(f"Unexpected API response: [{response.status}] {response.content}")
    
class ApiConnectionError(ApiError):
    """Raised when there was an error connecting to the API."""

    def __init__(self) -> None:
        super().__init__("Failed to establish a connection with the HTTP profiling API")