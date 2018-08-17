"""
A module to get information pending parcels.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import requests

class AfterShip:
    """This class is used to get parcel information from Aftership."""
    BASE_URL = 'https://api.aftership.com/v4'

    def __init__(self):
        """Initialize"""

    def get_trackings(self, api_key):
        """Get tracking information."""
        tracking_info = {}
        header = {'aftership-api-key': api_key, 'Content-Type':'application/json'}
        fetchurl = self.BASE_URL + '/trackings'
        try:
            tracking_request = requests.get(fetchurl, timeout=8, headers=header).json()['data']
            tracking_info = {'sucess': True, 'data': tracking_request}
        except:
            tracking_info = {'sucess': False}
        return tracking_info
