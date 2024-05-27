from src.api.controller import request, HTTPMethod, HTTPVersion
from src.error import ApiConnectionError

async def ping(version: HTTPVersion) -> bool:
    try:
        response = await request(version=version, method=HTTPMethod.GET, endpoint_path=[""])
    except ApiConnectionError:
        return False
    return response.status == 200