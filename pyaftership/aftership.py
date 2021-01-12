"""Main AfterShip object."""

from aiohttp import ClientSession

from .base import AfterShipBase
from .trackings import AfterShipTrackings


class AfterShip(AfterShipBase):
    """Main AfterShip object."""

    def __init__(self, api_key: str, session: ClientSession, timeout: int = 10) -> None:
        """Initialize."""
        self._api_key = api_key
        self._session = session
        self._timeout = timeout

        self.trackings = AfterShipTrackings()
