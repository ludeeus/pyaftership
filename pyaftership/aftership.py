"""Main AfterShip object."""

from typing import Optional

from aiohttp import ClientSession

from pyaftership.couriers import AfterShipCouriers

from .base import AfterShipBase
from .trackings import AfterShipTrackings


class AfterShip(AfterShipBase):
    """Main AfterShip object."""

    def __init__(self, api_key: str, session: ClientSession, timeout: int = 10) -> None:
        """Initialize."""
        AfterShipBase._api_key = api_key
        AfterShipBase._session = session
        AfterShipBase._timeout = timeout

        self.trackings = AfterShipTrackings()
        self.couriers = AfterShipCouriers()
