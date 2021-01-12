"""AfterShip Trackings object."""
from .base import AfterShipBase


class AfterShipTrackings(AfterShipBase):
    """AfterShip Trackings object."""

    async def list(self) -> dict:
        """
        List tracking information.

        https://docs.aftership.com/api/4/trackings/get-trackings
        """
        return await self._call_api("trackings")

    async def add(
        self,
        tracking_number: str,
        title: str = None,
        slug: str = None,
        tracking_postal_code: any = None,
    ) -> dict:
        """
        Add tracking information.

        https://docs.aftership.com/api/4/trackings/post-trackings
        """

        data = {"tracking": {"tracking_number": tracking_number}}

        if slug is not None:
            data["tracking"]["slug"] = slug

        if title is not None:
            data["tracking"]["title"] = title

        if tracking_postal_code is not None:
            data["tracking"]["tracking_postal_code"] = tracking_postal_code

        return await self._call_api("trackings", method="POST", data=data)

    async def remove(self, tracking_number: str, slug: str) -> dict:
        """
        Add tracking information.

        https://docs.aftership.com/api/4/trackings/delete-trackings
        """
        return await self._call_api(
            f"trackings/{slug}/{tracking_number}",
            method="DELETE",
            data={"tracking": {"tracking_number": tracking_number}},
        )
