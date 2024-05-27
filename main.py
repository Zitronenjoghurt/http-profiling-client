import asyncio
from src.api.resources.misc import ping

import logging
logging.basicConfig(level=logging.DEBUG)

async def test():
    success = await ping()
    print(success)

asyncio.run(test())