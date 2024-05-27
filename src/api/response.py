import httpx

class ApiResponse():
    def __init__(self, status: int, content: str) -> None:
        self.status = status
        self.content = content

    @staticmethod
    def from_httpx(response: httpx.Response) -> 'ApiResponse':
        return ApiResponse(status=response.status_code, content=response.content.decode())