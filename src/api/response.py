import http.client
import httpx
from datetime import datetime

class ApiResponse():
    def __init__(self, status: int, content: str) -> None:
        self.status = status
        self.content = content
        self.delay_ms = 0

    def set_delay(self, time_before: datetime, time_after: datetime):
        difference = (time_after - time_before)
        self.delay_ms = difference.total_seconds() * 1000

    @staticmethod
    def from_http(response: http.client.HTTPResponse) -> 'ApiResponse':
        return ApiResponse(status=response.status, content=response.read().decode())

    @staticmethod
    def from_httpx(response: httpx.Response) -> 'ApiResponse':
        return ApiResponse(status=response.status_code, content=response.content.decode())