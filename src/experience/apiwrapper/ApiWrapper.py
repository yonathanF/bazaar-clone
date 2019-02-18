"""
API Wrapper for the model layer so the experience layer can
communicate with it.
"""

import json

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
        try:
            response = requests.post(url, data=data)
            return response.status_code, response.json()
        except Exception as e:
            return json.dumps(
                {'Status': 'Failed to process request.[ %s ]' % (str(e))})

    def get(self, endpoint, data):
        url = self.base_url+endpoint
        try:
            response = requests.get(url)
            return response.status_code, response.json()

        except Exception as e:
            return json.dumps(
                {'Status': 'Failed to process request.[ %s ]' % (str(e))})


class APIV1(API):
    """
    A more concrete implementation that is aware of the v1
    endpoints. Avoids coupling with the exact urls such as /posts
    """
    pass
