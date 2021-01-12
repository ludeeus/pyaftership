"""AfterShip Base."""
import asyncio
from socket import gaierror
from typing import Optional, TYPE_CHECKING

import async_timeout
from aiohttp import ClientError, ClientResponse, ClientSession

from .const import BASE_URL
from .exceptions import AfterShipCommunicationException

if TYPE_CHECKING:
    from .trackings import AfterShipTrackings


class AfterShipBase:
    """Aftership Base object."""

    _api_key: str
    _session: ClientSession
    _timeout: int
    _trackings: Optional["AfterShipTrackings"]

    async def _call_api(
        self, endpoint: str, post: bool = False, data: Optional[dict] = None
    ) -> Optional[ClientResponse]:
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
                    json=data,
                )

        except asyncio.TimeoutError as exception:
            raise AfterShipCommunicationException("Timeout error") from exception

        except (ClientError, gaierror) as exception:
            raise AfterShipCommunicationException(
                f"Communication error {exception}"
            ) from exception
