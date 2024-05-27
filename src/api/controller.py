import httpx
from enum import Enum
from src.api.response import ApiResponse
from src.logging import LOGGER
from src.utils.api_operations import generate_url

class HTTPVersion(Enum):
    v1_0 = "HTTP/1.0"
    v1_1 = "HTTP/1.1"
    v2 = "HTTP/2"
    v3 = "HTTP/3"

class HTTPMethod(Enum):
    GET = "get"

async def request(version: HTTPVersion, method: HTTPMethod, endpoint_path: list[str], **kwargs) -> ApiResponse: # type: ignore
    url = generate_url(endpoint_path=endpoint_path, **kwargs)
    match version:
        case HTTPVersion.v1_1:
            match method:
                case HTTPMethod.GET:
                    response = await get_httpx(url=url)
        case HTTPVersion.v2:
            match method:
                case HTTPMethod.GET:
                    response = await get_httpx(url=url, http2=True)
    
    return response

async def get_httpx(url: str, http2: bool = False) -> ApiResponse:
    async with httpx.AsyncClient(http2=http2) as client:
        response = await client.get(url)
        return ApiResponse.from_httpx(response=response)