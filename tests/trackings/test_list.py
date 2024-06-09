"""Test list trackings."""

import aiohttp
import pytest

from pyaftership import AfterShip
from tests.common import API_KEY, load_fixture


@pytest.mark.asyncio
async def test_list(aresponses):
    """Test list trackings."""
    aresponses.add(
        "api.aftership.com",
        "/v4/trackings",
        "get",
        aresponses.Response(
            text=load_fixture("get_trackings"),
            status=200,
            headers={"Content-Type": "application/json"},
        ),
    )
    async with aiohttp.ClientSession() as session:
        aftership = AfterShip(API_KEY, session)
        trackings = await aftership.trackings.list()
        assert trackings["count"] != 0
        assert trackings["count"] == len(trackings["trackings"])
