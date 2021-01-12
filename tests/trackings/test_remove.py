"""Test remove tracking."""
import aiohttp
import pytest

from pyaftership import AfterShip
from tests.common import API_KEY, load_fixture


@pytest.mark.asyncio
async def test_remove(aresponses):
    """Test remove tracking."""
    aresponses.add(
        "api.aftership.com",
        "/v4/trackings/fedex/772857780801111",
        "delete",
        aresponses.Response(
            text=load_fixture("delete_trackings"),
            status=200,
            headers={"Content-Type": "application/json"},
        ),
    )
    async with aiohttp.ClientSession() as session:
        aftership = AfterShip(API_KEY, session)
        trackings = await aftership.trackings.remove(
            tracking_number="772857780801111", slug="fedex"
        )
        assert trackings["tracking"]["tracking_number"] == "772857780801111"
