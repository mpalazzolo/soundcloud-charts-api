from .api_base import APIBase
import requests
from bs4 import BeautifulSoup


class SoundCloudCharts(APIBase):

    def __init__(self, proxies=None):
        """
        Initialize the class. Calls the init method of APIBase and passes through root URL and proxy info.

        :param proxies: Dictionary of proxy information, if needed
        """
        super().__init__(root='https://api-v2.soundcloud.com/', proxies=proxies)
        self.client_id = self.get_client_id()  # Client ID needed to make API calls

    def get_client_id(self):
        """
        Gets the client ID for the API.
        The ID is located in a Javascript file that was found on the chart page source.
        The ID periodically will expire, so this function will look for the most recent ID upon initialization

        :return: Client ID as a string
        """
        # Client ID is in a JS file. These change periodically, so need to scan them all to find the Client ID
        r = requests.get('https://soundcloud.com/charts', proxies=self.proxies)
        soup = BeautifulSoup(r.text, 'html.parser')
        scripts = soup.findAll('script')
        links = []
        for script in scripts:
            try:
                links.append(script['src'])
            except KeyError:
                continue

        client_id = None
        # Loop through JS links to find the one that contains the client ID
        for link in links:
            # The file is large, so stream it and take just the first 10,000 characters
            # The ID is located within 10,000 characters, but this may need to change in the future
            chunk_size = 10000
            with requests.get(link, stream=True, proxies=self.proxies) as r:
                raw_text = next(r.iter_content(chunk_size=chunk_size)).decode('utf-8')

                pattern = 'client_id:"'
                len_of_id = 32  # The client ID is currently 32 characters long
                pattern_location = raw_text.find(pattern)
                if pattern_location == -1:
                    continue
                else:
                    start = pattern_location + len(pattern)
                    end = start + len_of_id
                    client_id = raw_text[start:end]
                    break

        return client_id

    def get_chart(self, kind='top', genre='all-music', region=None, limit=50, offset=0):
        """
        Get a Soundcloud chart

        :param kind: Chart type. Either "top" or "trending". "trending" is New & Hot
        :param genre: Song genre
        :param region: Country, or None for global
        :param limit: The maximum amount of songs to return
        :param offset: The index of the first item returned

        :return: JSON data of songs on chart
        """
        url = self.root + 'charts'
        if 'soundcloud:genres:' not in genre:
            genre = 'soundcloud:genres:' + genre

        if region is None:
            return self._get(url, client_id=self.client_id, kind=kind, genre=genre, limit=limit, offset=offset)
        else:
            if 'soundcloud:regions:' not in region:
                region = 'soundcloud:regions:' + region
            return self._get(url, client_id=self.client_id, kind=kind, genre=genre, region=region,
                             limit=limit, offset=offset)

