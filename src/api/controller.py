import http
import http.client
import httpx
from datetime import datetime
from enum import Enum
from src.api.response import ApiResponse
from src.config import Config
from src.logging import LOGGER
from src.utils.api_operations import generate_url, generate_path_with_params

CONFIG = Config.get_instance()

class HTTPVersion(Enum):
    v1_0 = "HTTP/1.0"
    v1_1 = "HTTP/1.1"
    v2 = "HTTP/2"
    v3 = "HTTP/3"

class HTTPMethod(Enum):
    GET = "get"

async def request(version: HTTPVersion, method: HTTPMethod, endpoint_path: list[str], **kwargs) -> ApiResponse: # type: ignore
    url = generate_url(endpoint_path=endpoint_path, **kwargs)
    time_before = datetime.now()
    match version:
        case HTTPVersion.v1_0:
            match method:
                case HTTPMethod.GET:
                    response = get_http(endpoint_path=endpoint_path, **kwargs)
        case HTTPVersion.v1_1:
            match method:
                case HTTPMethod.GET:
                    response = get_httpx(url=url)
        case HTTPVersion.v2:
            match method:
                case HTTPMethod.GET:
                    response = get_httpx(url=url, http2=True)
    time_after = datetime.now()
    response.set_delay(time_before=time_before, time_after=time_after)
    LOGGER.api_request(version=version.value, method=method.value, url=url, response=response)
    return response

def get_http(endpoint_path: list[str], **kwargs) -> ApiResponse:
    connection = http.client.HTTPSConnection(CONFIG.HOSTNAME)
    path = generate_path_with_params(endpoint_path=endpoint_path, **kwargs)
    connection.request("GET", path, headers={"Host": CONFIG.HOSTNAME, "Connection": "close"})
    response = connection.getresponse()
    connection.close()
    return ApiResponse.from_http(response)

def get_httpx(url: str, http2: bool = False) -> ApiResponse:
    with httpx.Client(http2=http2) as client:
        response = client.get(url)
        return ApiResponse.from_httpx(response=response)