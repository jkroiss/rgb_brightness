
from typing import List
from urllib import request

from src.color import Color

class ColorFactory:   
    
    @staticmethod
    def from_hex_list(color_list: List[str]) -> List[Color]:
        '''
        Function that takes a (hard-coded) list of hexedecimal rgb-values as input and creates a list of Color-objects out of it.      
        '''
        return [Color(hex_string) for hex_string in color_list] 

    @staticmethod
    def from_css_colors_api(url) -> List[Color]:
        '''
        Function that takes loads the hexedecimal rgb-values from the css-color-api and creates a list of Color-objects out of it.      
        '''
        try:
            req = request.Request(
                url, 
                headers={'User-Agent': 'ColorAnalyzer'}
            )
            with request.urlopen(req, timeout=100) as response:
                data = response.read().decode('utf-8')
                colors = json.loads(data)['colors']
        except Exception as e:
            raise ValueError(f'Failed to get colors from API: {e}')
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