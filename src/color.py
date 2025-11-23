import math

from typing import Tuple

class Color:
    # Since Color is re-used for creating Color-objects from the given api as well, 'hex_string' is the only non-optional parameter.
    def __init__(self, hex_string: str, name: str | None = None, theme: str | None = None, group: str | None = None, 
                 rgb_string: str | None = None):
        self.hex_string = hex_string
        self.r, self.g, self.b = self._parse_hex_string(self.hex_string)

        # In the following attributes, additional information is stored, if something like an api provides it.
        self.name = name
        self.theme = theme
        self.group = group
        self.rgb_string = rgb_string

    def get_brightness(self) -> float:
        ''' Calculates the brightness of a color based on the given formula using color rgb-values.'''
        
        color_brightness = math.sqrt(0.241 * self.r**2 + 0.691 * self.g**2 + 0.068 * self.b**2)
        return color_brightness

    def _parse_hex_string(self, hex_string: str) -> Tuple[int, int, int]:
        '''Private function that parse a string containing the hexadecimal rgb-values and returns them as integer values'''
        hex_string = hex_string.strip('#').upper()

        if len(hex_string) == 3:
            hex_string = ''.join([hex_char*2 for hex_char in hex_string])
        
        # Check here, whether it is a valid hexadecimal rgb-representation, as such a representation should be 6 characters long, bar the '#'.
        if len(hex_string) != 6:
            raise ValueError("Incorrect hexadecimal representation of RGB-values.")
            
        r = int(hex_string[:2], 16)
        g = int(hex_string[2:4], 16)
        b = int(hex_string[4:], 16)
        return r, g, b