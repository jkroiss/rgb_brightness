import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import unittest
import math
from src.color import Color

class TestColor(unittest.TestCase):
    """Tests for the Color-class."""
    def test_parse_full_hex_string(self):
        """Tests the parsing of a string containing a full hexadecimal representation of an RGB-value."""
        hex_string = '#AABBCC'
        color = Color(hex_string)
        self.assertEqual(color.r, 170)
        self.assertEqual(color.g, 187)
        self.assertEqual(color.b, 204)

    def test_parse_short_hex_string(self):
        """Tests the parsing of a string containing a shortened hexadecimal representation of an RGB-value."""
        hex_string = '#ABC'
        color = Color(hex_string)
        self.assertEqual(color.r, 170)
        self.assertEqual(color.g, 187)
        self.assertEqual(color.b, 204)

    def test_parse_hex_string_without_hash(self):
        """Tests the parsing of a hexadecimal string representing RGB-values without the leading hash."""
        hex_string = 'AABBCC'
        color = Color(hex_string)
        self.assertEqual(color.r, 170)
        self.assertEqual(color.g, 187)
        self.assertEqual(color.b, 204)

    def test_invalid_hex_string_characters(self):
        """Tests Error handling for strings with characters outside of the hexadecimal range."""
        with self.assertRaisesRegex(ValueError, "Invalid hexadecimal representation."):
            Color('#JJJJJJ')
    
    def test_invalid_hex_string_length(self):
        """Tests Error handling for strings of incorrect lengths (i.e. not 3 or 6 hexadecimal digits)"""
        with self.assertRaisesRegex(ValueError, "Incorrect hexadecimal representation of RGB-values."):
            Color('#1A')
        
        with self.assertRaisesRegex(ValueError, "Incorrect hexadecimal representation of RGB-values."):
            Color('#1234567')

    def test_brightness_calculation(self):
        """Tests the brightness calculation."""
        color = Color('#AABBCC')
        r = 170
        g = 187
        b = 204
        expected_brightness = math.sqrt(0.241 * r**2 + 0.691 * g**2 + 0.068 * b**2)
        self.assertAlmostEqual(color.get_brightness(), expected_brightness)

    def test_optional_attributes(self):
        """Tests whether the optional attributes are set correctly."""
        color = Color(
            '#AABBCC',
            name='Test Color',
            theme='Test Theme',
            group='Test Group',
            rgb_string='170,187,204' 
        )
        self.assertEqual(color.name, 'Test Color')
        self.assertEqual(color.theme, 'Test Theme')
        self.assertEqual(color.group, 'Test Group')
        self.assertEqual(color.rgb_string, '170,187,204')


if __name__ == '__main__':
    unittest.main()