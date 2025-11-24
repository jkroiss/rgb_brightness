import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import unittest
import json
from urllib import request
from src.brightness_comparer import BrightnessComparer
from src.color_factory import ColorFactory
from src.color import Color

class TestBrightnessComparer(unittest.TestCase):
    ''' 
    Tests for the BrightnesComparer class.
    
    Tests the retrieval of the brightest color and the formatting of it.
    '''
    def test_get_brightest_color(self):
        '''Tests the retrieval of the brightest color.'''
        hex_list = ['#AABBCC', '#DDEEFF', '#FFFFFF']
        colors = ColorFactory.from_hex_list(hex_list)
        brightest = BrightnessComparer.get_brightest_color(colors)
        self.assertEqual(brightest.hex_string.upper(), '#FFFFFF')

    def test_format_brightest_color_without_name(self):
        '''Test the formatting of the brightest color without a name.'''
        color = Color('#AABBCC')
        formatted = BrightnessComparer.format_brightest_color(color)
        expected = 'The brightest color is: #AABBCC (r=170, g=187, b=204)'
        self.assertEqual(formatted, expected)

    def test_format_brightest_color_with_name(self):
        '''Test the formatting of the brightest color with a name.'''
        color = Color('#AABBCC', name='Test Color')
        formatted = BrightnessComparer.format_brightest_color(color)
        expected = 'The brightest color is: #AABBCC (r=170, g=187, b=204), called "Test Color"'
        self.assertEqual(formatted, expected)


if __name__ == '__main__':
    unittest.main()