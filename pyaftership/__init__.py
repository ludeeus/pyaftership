"""
A module to get information pending parcels.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import requests
import json

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
            tracking_info = {'success': True, 'data': tracking_request}
        except:
            tracking_info = {'success': False}
        return tracking_info

    def add_tracking(self, api_key, slug, title, tracking_number):
        """Add tracking information."""
        tracking_info = {}
        header = {'aftership-api-key': api_key, 'Content-Type':'application/json'}
        url = self.BASE_URL + '/trackings'
        tracking = {
            'tracking': {
                'slug': slug,
                'tracking_number': tracking_number,
                'title': title,
            }
        }
        try:
            requests.post(url, timeout=8, data=json.dumps(tracking), headers=header)
            tracking_info = {'success': True}
        except:
            tracking_info = {'success': False}
        return tracking_info
