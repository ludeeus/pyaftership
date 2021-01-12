"""AfterShip Couriers object."""
from .base import AfterShipBase


class AfterShipCouriers(AfterShipBase):
    """AfterShip Couriers object."""

    async def detect(self, tracking_number: str, **kwargs) -> dict:
        """
        Detect couriers for tracking number.

        https://docs.aftership.com/api/4/couriers/post-couriers-detect
        """
        data = {"tracking": kwargs}
        data["tracking"]["tracking_number"] = tracking_number

        return await self._call_api("couriers/detect", method="POST", data=data)
