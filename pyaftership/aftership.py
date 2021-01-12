"""Main AfterShip object."""
import asyncio
from socket import gaierror
from typing import Optional

import aiohttp
import async_timeout

from .const import BASE_URL, GOOD_HTTP_CODES
from .exceptions import AfterShipCommunicationException, AfterShipException


class AfterShip:
    """Main AfterShip object."""

    def __init__(
        self, api_key: str, session: aiohttp.ClientSession, timeout: int = 10
    ) -> None:
        """Initialize."""
        self._api_key = api_key
        self._session = session
        self._timeout = timeout

    async def get_trackings(self):
        """Get tracking information."""
        response = await self._call_api("trackings")

        if not response:
            raise AfterShipException()

        if response.status not in GOOD_HTTP_CODES:
            meta = response.get("meta", {})
            raise AfterShipCommunicationException(
                f"{response.status} is not valid - {meta.get('code')} - {meta.get('message')}"
            )

        result = await response.json()
        return result.get("data", [])

    async def _call_api(
        self, endpoint: str, post: bool = False
    ) -> Optional[aiohttp.ClientResponse]:
        """Private method to call the AfterShip API."""
        try:
            async with async_timeout.timeout(self._timeout):
                return await self._session.request(
                    method="POST" if post else "GET",
                    url=f"{BASE_URL}/{endpoint}",
                    headers={
                        "aftership-api-key": self._api_key,
                        "Content-Type": "application/json",
                    },
                )

        except asyncio.TimeoutError as exception:
            raise AfterShipCommunicationException("Timeout error") from exception

        except (aiohttp.ClientError, gaierror) as exception:
            raise AfterShipCommunicationException(
                f"Communication error {exception}"
            ) from exception
