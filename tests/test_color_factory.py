import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import ssl
import json
import unittest

from urllib import request
from src.color_factory import ColorFactory
from src.color import Color

class TestColorFactory(unittest.TestCase):
    """Tests for the ColorFactory-class."""

    def setUp(self) -> None:
        """Setup for the tests."""
        # Note: macOS workaround for SSL certificate verification; local development only
        self.context = ssl._create_unverified_context()

    def test_from_hex_list(self) -> None:
        """Tests the correct creation of Color-objects from a list of rgb-values in hexadecimal representation."""
        hex_list = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
        colors = ColorFactory.from_hex_list(hex_list)
        self.assertEqual(len(colors), 5)
        for element in colors:
            self.assertIsInstance(element, Color)

    def test_from_css_colors_api_all(self) -> None:
        """Tests the correct creation of Color-objects from the css-colors API."""
        url = "https://csscolorsapi.com/api/colors" 
        req = request.Request(url, headers={'User-Agent': 'BrightnessComparer'})
        with request.urlopen(req, timeout=10, context=self.context) as response:
            data = response.read().decode('utf-8')
            colors_from_api = json.loads(data)['colors']
        colors = ColorFactory.from_css_colors_api(url)
        self.assertEqual(len(colors), len(colors_from_api))
        for element in colors:
            self.assertIsInstance(element, Color)

    def test_from_css_colors_api_group(self) -> None:
        """Tests the correct creation of Color-objects from a group from the css-colors API."""
        url = "https://csscolorsapi.com/api/colors/group/blue" 
        req = request.Request(url, headers={'User-Agent': 'BrightnessComparer'})
        with request.urlopen(req, timeout=10, context=self.context) as response:
            data = response.read().decode('utf-8')
            colors_from_api = json.loads(data)['colors']
        colors = ColorFactory.from_css_colors_api(url)
        self.assertEqual(len(colors), len(colors_from_api))
        for element in colors:
            self.assertIsInstance(element, Color)

    def test_from_css_colors_api_single_color(self) -> None:
        """Tests the correct creation of a single color from the CSS colors API."""
        url = "https://csscolorsapi.com/api/colors/CadetBlue" 
        req = request.Request(url, headers={'User-Agent': 'BrightnessComparer'})
        with request.urlopen(req, timeout=10, context=self.context) as response:
            data = response.read().decode('utf-8')
            colors_from_api = [json.loads(data)['data']]
        colors = ColorFactory.from_css_colors_api(url)
        self.assertEqual(len(colors), len(colors_from_api))
        for element in colors:
            self.assertIsInstance(element, Color)

    def test_from_css_colors_api_theme(self) -> None:
        """Tests the correct creation of Color-objects from a theme from the css-colors API."""
        url = "https://csscolorsapi.com/api/colors/theme/dark" 
        req = request.Request(url, headers={'User-Agent': 'BrightnessComparer'})
        with request.urlopen(req, timeout=10, context=self.context) as response:
            data = response.read().decode('utf-8')
            colors_from_api = json.loads(data)['colors']
        colors = ColorFactory.from_css_colors_api(url)
        self.assertEqual(len(colors), len(colors_from_api))
        for element in colors:
            self.assertIsInstance(element, Color)
    
    def test_from_css_colors_api_with_invalid_url(self) -> None:
        """Tests the Error handling when using an invalid url."""
        url = "https://invalid_test_url_for_from_css_colors_api_1337_42.com/api/colors"
        with self.assertRaisesRegex(ValueError, "Failed to get data from the API: .*"):
            ColorFactory.from_css_colors_api(url)


if __name__ == '__main__':
    unittest.main()