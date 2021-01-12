"""AfterShip Trackings object."""

from .base import AfterShipBase
from .const import GOOD_HTTP_CODES
from .exceptions import AfterShipCommunicationException, AfterShipException


class AfterShipTrackings(AfterShipBase):
    """AfterShip Trackings object."""

    async def list_trackings(self):
        """List tracking information."""
        response = await self._call_api("trackings")

        if not response:
            raise AfterShipException()

        if response.status not in GOOD_HTTP_CODES:
            meta = response.get("meta", {})
            raise AfterShipCommunicationException(
                f"{response.status} is not valid - {meta.get('code')} - {meta.get('message')}"
            )

        result = await response.json()
        return result.get("data", {})

    async def add_tracking(
        self,
        tracking_number: str,
        title: str = None,
        slug: str = None,
        tracking_postal_code: str = None,
    ):
        """Add tracking information."""

        data = {"tracking": {"tracking_number": tracking_number}}

        if slug is not None:
            data["tracking"]["slug"] = slug

        if title is not None:
            data["tracking"]["title"] = title

        if tracking_postal_code is not None:
            data["tracking"]["tracking_postal_code"] = tracking_postal_code

        response = await self._call_api("trackings", post=True, data=data)

        if not response:
            raise AfterShipException()

        if response.status not in GOOD_HTTP_CODES:
            meta = response.get("meta", {})
            raise AfterShipCommunicationException(
                f"{response.status} is not valid - {meta.get('code')} - {meta.get('message')}"
            )

        result = await response.json()
        return result.get("data", {})
