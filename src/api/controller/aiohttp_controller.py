import aiohttp
from typing import Optional
from src.api.response import ApiResponse
from src.error import ApiConnectionError, UnexpectedApiError
from src.logging import LOGGER
from src.utils.api_operations import generate_url

async def get(endpoint_path: list[str], headers: Optional[dict] = None, **params) -> ApiResponse:
    url = generate_url(endpoint_path, **params)

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                content = await response.text()
                LOGGER.api_request("GET", url, response.status, content)
                return ApiResponse(response.status, content)
    except aiohttp.ClientConnectionError:
        raise ApiConnectionError()
    
async def get_image(file_path: str, endpoint_path: list[str], headers: Optional[dict] = None, **params):
    url = generate_url(endpoint_path, **params)

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    image_data = await response.read()
                    with open(file_path, 'wb') as image_file:
                        image_file.write(image_data)
                    LOGGER.api_request("GET", url, response.status, "Image downloaded")
                else:
                    LOGGER.api_request("GET", url, response.status, "Failed to download image")
                    raise UnexpectedApiError(response=response)
    except aiohttp.ClientConnectionError:
        raise ApiConnectionError()
        
async def post(endpoint_path: list[str], headers: Optional[dict] = None, **params) -> ApiResponse:
    url = generate_url(endpoint_path, **params)

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(url) as response:
                content = await response.text()
                LOGGER.api_request("POST", url, response.status, content)
                return ApiResponse(response.status, content)
    except aiohttp.ClientConnectionError:
        raise ApiConnectionError()