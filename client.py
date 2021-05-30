import requests

from errors import PrimaryServerException


class Client:
    def __init__(self, result_no):
        self.uri = 'https://web.thetaporlando.com/apps/getItemsByCategorie/' + result_no + '/0'

    def get(self):
        response = requests.get(self.uri)
        if response.status_code == 200:
            return response.json()
        else:
            raise PrimaryServerException("Primary server is down")
