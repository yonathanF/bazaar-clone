"""
API Wrapper for the model layer so the experience layer can
communicate with it.
"""

import requests

BASE_URL = "http://models-api:8000/api/v1"


class API(object):
    """
    Wraps the URL and provides basic methods to communicate to it
    """
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def post(self, endpoint, data):
        url = self.base_url+endpoint
        response = requests.post(url, data=data)
        return response.json()

    def get(self, endpoint, data):
        url = self.base_url+endpoint
        response = requests.get(url)
        return response.json()
