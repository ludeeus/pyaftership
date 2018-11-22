"""Example usage of pyaftership."""
import asyncio
import aiohttp
from pyaftership.tracker import Tracking

API_KEY = 'JFNDKUS73438798FJH38Y9FHH38F9FHQO789'


async def example():
    """Get pending packages."""
    async with aiohttp.ClientSession() as session:
        pyaftership = Tracking(LOOP, session, API_KEY)
        packages = await pyaftership.get_trackings()
        print("Pending packages:", packages)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(example())
