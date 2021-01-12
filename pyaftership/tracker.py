"""
Python wrapper package for the AfterShip API.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import asyncio
import logging
import socket

import aiohttp
import async_timeout

from pyaftership.const import GOOD_HTTP_CODES, URL

_LOGGER = logging.getLogger(__name__)


class Tracking(object):
    """A class for the Traccar API."""

    def __init__(self, loop, session, api_key):
        """Initialize the class."""
        self._loop = loop
        self._session = session
        self.api_key = api_key
        self._trackings = {}
        self._meta = {}

    async def get_trackings(self):
        """Get tracking information."""
        self._trackings = {}
        self._meta = {}
        headers = {
            "aftership-api-key": self.api_key,
            "Content-Type": "application/json",
        }
        url = "{}/trackings".format(URL)
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                response = await self._session.get(url, headers=headers)
                result = await response.json()
                try:
                    if response.status in GOOD_HTTP_CODES:
                        self._trackings = result["data"]
                    else:
                        _LOGGER.error(
                            "Error code %s - %s",
                            result["meta"]["code"],
                            result["meta"]["message"],
                        )
                    self._meta = result["meta"]
                except (TypeError, KeyError) as error:
                    _LOGGER.error("Error parsing data from AfterShip, %s", error)
        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error("Error connecting to AfterShip, %s", error)
        return self._trackings

    async def add_package_tracking(
        self, tracking_number, title=None, slug=None, tracking_postal_code=None
    ):
        """Add tracking information."""
        headers = {
            "aftership-api-key": self.api_key,
            "Content-Type": "application/json",
        }
        url = "{}/trackings".format(URL)
        data = {}
        data["tracking"] = {}
        data["tracking"]["tracking_number"] = tracking_number
        if slug is not None:
            data["tracking"]["slug"] = slug
        if title is not None:
            data["tracking"]["title"] = title
        if tracking_postal_code is not None:
            data["tracking"]["tracking_postal_code"] = tracking_postal_code
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                await self._session.post(url, headers=headers, json=data)
        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error("Error connecting to AfterShip, %s", error)

    async def remove_package_tracking(self, slug, tracking_number):
        """Delete tracking information."""
        headers = {
            "aftership-api-key": self.api_key,
            "Content-Type": "application/json",
        }
        url = "{}/trackings/{}/{}".format(URL, slug, tracking_number)
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                await self._session.delete(url, headers=headers)
        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error("Error connecting to AfterShip, %s", error)

    async def detect_couriers_for_tracking_number(self, tracking_number, **kwargs):
        """
        Detect couriers for tracking number.

        Add any optional parameters as kwargs when calling the method.
        An overview can be found at
        https://docs.aftership.com/api/4/couriers/post-couriers-detect
        """
        headers = {
            "aftership-api-key": self.api_key,
            "Content-Type": "application/json",
        }
        url = "{}/couriers/detect".format(URL)
        data = {}
        data["tracking"] = kwargs
        data["tracking"]["tracking_number"] = tracking_number
        couriers = {}
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                response = await self._session.post(url, headers=headers, json=data)
                result = await response.json()
                try:
                    if response.status in GOOD_HTTP_CODES:
                        couriers = result["data"]
                    else:
                        _LOGGER.error(
                            "Error code %s - %s",
                            result["meta"]["code"],
                            result["meta"]["message"],
                        )
                except (TypeError, KeyError) as error:
                    _LOGGER.error("Error parsing data from AfterShip, %s", error)
        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error("Error connecting to Aftership, %s", error)
        return couriers

    @property
    def trackings(self):
        """Return all trackings."""
        return self._trackings

    @property
    def meta(self):
        """Return the last meta response."""
        return self._meta
