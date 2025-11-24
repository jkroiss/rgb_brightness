
import ssl
import json

from typing import List
from urllib import request
from urllib.error import URLError

from src.color import Color

class ColorFactory:   
    '''Factory-type class for creating collections of Color-objects from different sources.'''
    @staticmethod
    def from_hex_list(color_list: List[str]) -> List[Color]:
        '''Function that creates a list of Color-objects from a list of hex-strings.'''
        return [Color(hex_string) for hex_string in color_list] 

    @staticmethod
    def from_css_colors_api(url: str) -> List[Color]:
        '''
        Function that creates a list of Color-objects from the CSS colors API.

        Args:
            url (str): The url of the CSS colors API.
        
        Returns: 
            List[Color]: The list of the created Color-objects.

        Raises: 
            ValueError: If the url or the json format is invalid.
        '''
        try:
            # Note: macOS workaround for SSL certificate verification; local development only
            context = ssl._create_unverified_context()
            req = request.Request(url, headers={'User-Agent': 'ColorAnalyzer'})
            with request.urlopen(req, timeout=10, context=context) as response:
                data = response.read().decode('utf-8')
                colors = json.loads(data)['colors']
        except URLError as e:
            raise ValueError(f"Failed to get data from the API: {e}") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse json from the API: {e}") from e
        
        return [
            Color(
                color.get('hex'),
                name=color.get('name'),
                theme=color.get('theme'),
                group=color.get('group'),
                rgb_string=color.get('rgb')
            ) 
            for color in colors
        ]