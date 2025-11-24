import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import unittest
import json
from urllib import request
from src.color_factory import ColorFactory
from src.color import Color

class TestColorFactory(unittest.TestCase):
    def test_from_hex_list(self):
        hex_list = ['#AABBCC', '#123456', '#FFFFFF']
        colors = ColorFactory.from_hex_list(hex_list)
        self.assertEqual(len(colors), 3)
        for element in colors:
            self.assertIsInstance(element, Color)

    def test_from_css_colors_api(self):
        url = "https://csscolorsapi.com/api/colors"
        req = request.Request(
                url, 
                headers={'User-Agent': 'ColorAnalyzer'}
            )
        with request.urlopen(req, timeout=100) as response:
            data = response.read().decode('utf-8')
            colors_from_api = json.loads(data)['colors']
        colors = ColorFactory.from_css_colors_api(url)
        self.assertEqual(len(colors), len(colors_from_api))
        self.assertEqual(len(colors), 3)
        for element in colors:
            self.assertIsInstance(element, Color)

if __name__ == '__main__':
    unittest.main()