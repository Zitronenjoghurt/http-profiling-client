import asyncio
from src.api.controller import HTTPVersion
from src.api.resources.misc import ping

import logging
logging.basicConfig(level=logging.DEBUG)

async def test():
    success = await ping(version=HTTPVersion.v2)
    print(success)

asyncio.run(test())