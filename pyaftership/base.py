"""AfterShip Base."""
import asyncio
from socket import gaierror
from typing import Optional, TYPE_CHECKING

import async_timeout
from aiohttp import ClientError, ClientResponse, ClientSession

from .const import BASE_URL, GOOD_HTTP_CODES
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
        self, endpoint: str, method: str = "GET", data: Optional[dict] = None
    ) -> Optional[ClientResponse]:
        """Private method to call the AfterShip API."""
        try:
            async with async_timeout.timeout(self._timeout):
                response = await self._session.request(
                    method=method,
                    url=f"{BASE_URL}/{endpoint}",
                    headers={
                        "aftership-api-key": self._api_key,
                        "Content-Type": "application/json",
                    },
                    json=data,
                )
                return await self._handle_response(response)

        except asyncio.TimeoutError as exception:
            raise AfterShipCommunicationException("Timeout error") from exception

        except (ClientError, gaierror) as exception:
            raise AfterShipCommunicationException(
                f"Communication error {exception}"
            ) from exception

    async def _handle_response(self, response: ClientResponse) -> Optional[dict]:
        """Private method handle the result from AfterShip."""
        result = await response.json() if response else {}

        if response.status not in GOOD_HTTP_CODES:
            meta = result.get("meta", {})
            raise AfterShipCommunicationException(
                f"{response.status} is not valid - {meta.get('code')} - {meta.get('message')}"
            )

        return result.get("data", {})
