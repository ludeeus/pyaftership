"""Test add trackings."""
import aiohttp
import pytest

from pyaftership import AfterShip
from tests.common import API_KEY, load_fixture


@pytest.mark.asyncio
async def test_add_trackings(aresponses):
    """Test add trackings."""
    aresponses.add(
        "api.aftership.com",
        "/v4/trackings",
        "post",
        aresponses.Response(
            text=load_fixture("post_trackings"),
            status=201,
            headers={"Content-Type": "application/json"},
        ),
    )
    async with aiohttp.ClientSession() as session:
        aftership = AfterShip(API_KEY, session)
        trackings = await aftership.trackings.add_tracking(
            tracking_number="1111111111111"
        )
        assert trackings["tracking"]["tracking_number"] == "1111111111111"
