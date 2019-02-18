import os
import requests

BAZAAR_API_KEY = os.environ.get('BAZAAR_API_KEY', None)

class APIKeyMissingError(Exception):
	pass

if BAZAAR_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. "
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = BAZAAR_API_KEY

from .post import Post