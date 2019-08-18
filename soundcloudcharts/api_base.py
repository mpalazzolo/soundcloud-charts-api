import requests
from requests.exceptions import HTTPError
import time


class APIBase:
    """
    This class is to be used as a base to build an API library.
    Authorization token generation and endpoint functions must be written
    """

    def __init__(self, root, proxies=None, requests_session=True, max_retries=10, requests_timeout=None):
        """
        Initialize the class

        :param: root: Root URL for the API
        :param proxies: A dictionary of proxies, if needed
        :param requests_session: Use request Sessions class. Speeds up API calls significantly when set to True
        :param max_retries: Maximum amount of times to retry an API call before stopping
        :param requests_timeout: Number of seconds requests should wait before timing out
        """

        self.proxies = proxies
        self.token_str = ""  # Encrypted API token. This will need to be set manually or by a method of a subclass
        self.root = root
        self.max_retries = max_retries
        self.requests_timeout = requests_timeout
        if requests_session:
            self._session = requests.Session()
        else:
            self._session = requests.api  # individual calls, slower

    def _auth_headers(self):
        """
        Get header for API request

        :return: header in dictionary format
        """
        if self.token_str:
            return {'Authorization': 'Bearer {}'.format(self.token_str)}
        else:
            return {}

    def _call(self, method, url, params):
        """
        Make a call to the API

        :param method: 'GET', 'POST', 'DELETE', or 'PUT'
        :param url: URL of API endpoint
        :param params: API paramaters

        :return: JSON data from the API
        """
        if not url.startswith('http'):
            url = self.root + url
        headers = self._auth_headers()
        headers['Content-Type'] = 'application/json'

        r = self._session.request(method, url,
                                  headers=headers,
                                  proxies=self.proxies,
                                  params=params,
                                  timeout=self.requests_timeout)
        r.raise_for_status()  # Check for error
        return r.json()

    def _get(self, url, **kwargs):
        """
        GET request from the API

        :param url: URL for API endpoint

        :return: JSON data from the API
        """
        retries = self.max_retries
        delay = 1
        while retries > 0:
            try:
                return self._call('GET', url, kwargs)
            except HTTPError as e:  # Retry for some known issues
                retries -= 1
                status = e.response.status_code
                if status == 429 or (500 <= status < 600):
                    if retries < 0:
                        raise
                    else:
                        sleep_seconds = int(e.headers.get('Retry-After', delay))
                        print('retrying ...' + str(sleep_seconds) + ' secs')
                        time.sleep(sleep_seconds + 1)
                        delay += 1
                else:
                    raise
            except Exception as e:
                print('exception', str(e))
                retries -= 1
                if retries >= 0:
                    print('retrying ...' + str(delay) + 'secs')
                    time.sleep(delay + 1)
                    delay += 1
                else:
                    raise

    def _post(self, url, **kwargs):
        """
        POST request from the API

        :param url: URL for API endpoint

        :return: JSON data from the API
        """
        return self._call('POST', url, kwargs)

    def _delete(self, url, **kwargs):
        """
        DELETE request from the API

        :param url: URL for API endpoint

        :return: JSON data from the API
        """
        return self._call('DELETE', url, kwargs)

    def _put(self, url, **kwargs):
        """
        PUT request from the API

        :param url: URL for API endpoint

        :return: JSON data from the API
        """
        return self._call('PUT', url, kwargs)