"""Example usage of pyaftership."""
import asyncio

import aiohttp

from pyaftership.tracker import Tracking

API_KEY = "JFNDKUS73438798FJH38Y9FHH38F9FHQO789"


async def example():
    """Get pending packages."""
    async with aiohttp.ClientSession() as session:
        pyaftership = Tracking(LOOP, session, API_KEY)
        packages = await pyaftership.get_trackings()
        print("Pending packages:", packages)


async def detect_couriers_example():
    """Detect couriers for tracking number."""
    async with aiohttp.ClientSession() as session:
        pyaftership = Tracking(LOOP, session, API_KEY)
        tracking_number = "1Z9999999999999999"
        couriers = await pyaftership.detect_couriers_for_tracking_number(
            tracking_number
        )
        print("Possible couriers:", couriers)


asyncio.get_event_loop().run_until_complete(example())
asyncio.get_event_loop().run_until_complete(detect_couriers_example())
