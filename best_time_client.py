import requests

from errors import PrimaryServerException


class BestTimeClient:
    def __init__(self, api_key_private):
        self.uri = 'https://besttime.app/api/v1/forecasts'
        self.api_key_private = api_key_private

    def get(self, venue_name, venue_address):
        querystring = {
            "api_key_private": self.api_key_private,
            "venue_name": venue_name,
            "venue_address": venue_address
        }
        response = requests.request("POST", self.uri, headers={}, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            raise PrimaryServerException("Best time server is down")
