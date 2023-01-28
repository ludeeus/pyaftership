"""Test base."""
import asyncio
from unittest.mock import patch

import aiohttp
import pytest

from pyaftership import AfterShip, AfterShipException
from tests.common import API_KEY, load_fixture


@pytest.mark.asyncio
async def test_base_none_valid_code(aresponses):
    """Test base."""
    aresponses.add(
        "api.aftership.com",
        "/v4/trackings",
        "get",
        aresponses.Response(
            text=load_fixture("error_server_is_down"),
            status=500,
            headers={"Content-Type": "application/json"},
        ),
    )
    async with aiohttp.ClientSession() as session:
        aftership = AfterShip(API_KEY, session)
        with pytest.raises(AfterShipException):
            await aftership.trackings.list()


@pytest.mark.asyncio
async def test_base_exceptions(aresponses):
    """Test base."""
    async with aiohttp.ClientSession() as session:
        aftership = AfterShip(API_KEY, session)
        with pytest.raises(AfterShipException):
            await aftership.trackings.list()

        aftership = AfterShip(API_KEY, session, 0)
        with patch(
            "pyaftership.base.AfterShipBase._session.request",
            side_effect=asyncio.TimeoutError,
        ):
            with pytest.raises(AfterShipException):
                await aftership.trackings.list()
