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
from pyaftership.const import URL, HEADERS

_LOGGER = logging.getLogger(__name__)


class Tracking(object):
    """A class for the Traccar API."""

    def __init__(self, loop, session, api_key):
        """Initialize the class."""
        self._loop = loop
        self._session = session
        self.api_key = api_key
        self._pending_packages = {}

    async def get_pending_packages(self):
        """Get tracking information."""
        headers = HEADERS.format(api_key=self.api_key)
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                response = await self._session.get(URL, headers=headers)
                self._pending_packages = await response.json()
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to AfterShip, %s', error)
        return self._pending_packages

    async def add_package_tracking(self, tracking_number, title='Package',
                                   slug=None):
        """Add tracking information."""
        headers = HEADERS.format(api_key=self.api_key)
        data = {
            'tracking': {
                'slug': slug,
                'tracking_number': tracking_number,
                'title': title
            }
        }
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                await self._session.post(URL, headers=headers, json=data)
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to AfterShip, %s', error)

    async def remove_package_tracking(self, slug, tracking_number):
        """Delete tracking information."""
        headers = HEADERS.format(api_key=self.api_key)
        url = "{}/{}/{}".format(URL, slug, tracking_number)
        try:
            async with async_timeout.timeout(8, loop=self._loop):
                await self._session.delete(url, headers=headers)
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to AfterShip, %s', error)


    @property
    def pending_packages(self):
        """Return the device info if any."""
        return self._pending_packages
