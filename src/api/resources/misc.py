from src.api.controller.aiohttp_controller import get
from src.error import ApiConnectionError

async def ping() -> bool:
    try:
        response = await get(endpoint_path=[""])
    except ApiConnectionError:
        return False
    return response.status == 200