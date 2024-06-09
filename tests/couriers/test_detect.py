"""Test detect couriers."""

import aiohttp
import pytest

from pyaftership import AfterShip
from tests.common import API_KEY, load_fixture


@pytest.mark.asyncio
async def test_detect(aresponses):
    """Test detect couriers."""
    aresponses.add(
        "api.aftership.com",
        "/v4/couriers/detect",
        "post",
        aresponses.Response(
            text=load_fixture("post_couriers_detect"),
            status=200,
            headers={"Content-Type": "application/json"},
        ),
    )
    async with aiohttp.ClientSession() as session:
        aftership = AfterShip(API_KEY, session)
        trackings = await aftership.couriers.detect(tracking_number="1111111111111")
        assert trackings["total"] == 2
