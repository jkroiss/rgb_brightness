import math

from typing import Tuple

class Color:
    '''
    Class representing a color with optional metadata.

    Attributes:
        hex_string (str): Hexadecimal string representing the actual color.
        r (int): Red color component.
        g (int): Green color component.
        b (int): Blue color component.
        name (str | None): Optional name of the color.
        theme (str | None): Optional theme of the color.
        group (str | None): Optional group of the color.)
        rgb_string (str | none): Optional string representing the rgb-values, e.g. '255,0,0' for red.
    '''

    def __init__(self, hex_string: str, name: str | None = None, theme: str | None = None, group: str | None = None, 
                 rgb_string: str | None = None):
        '''Initializes a Color-object with optional metadata.'''

        self.hex_string = hex_string
        self.r, self.g, self.b = self._parse_hex_string(self.hex_string)

        # In the following attributes, additional information is stored, if something like an api provides it.
        self.name = name
        self.theme = theme
        self.group = group
        self.rgb_string = rgb_string

    def get_brightness(self) -> float:
        ''' 
        Calculates the brightness of a color based on its' rgb-values. 
        
        Uses the forumla: sqrt(0.241 * R^2 + 0.691 * G^2 + 0.068 * B^2)     

        Returns:
            float: The brightness of the color.    
        '''
        
        color_brightness = math.sqrt(0.241 * self.r**2 + 0.691 * self.g**2 + 0.068 * self.b**2)
        return color_brightness

    def _parse_hex_string(self, hex_string: str) -> Tuple[int, int, int]:
        '''
        Converts a string containing a hexadecimal representation of rgb-values into its' integer components.

        Supports:
            - Full hexadecimal represention, e.g. '#RRGGBB' or 'RRGGBB'.
            - Short hexadecimal representation, e.g. '#RGB' or 'RGB'', which is then expanded.

        Args: 
            hex_string (str): Hexadecimal string representation of the color.

        Returns:
            Tuple[int, int, int]: The rgb-values of the color as integers. 

        Raises:
            ValueError: If the string does no contain a supported hexadecimal representation.
        '''
        hex_string = hex_string.strip('#').upper()

        if len(hex_string) == 3:
            hex_string = ''.join([hex_char*2 for hex_char in hex_string])
        
        # Check here, whether it is a valid hexadecimal rgb-representation.
        if len(hex_string) != 6:
            raise ValueError("Incorrect hexadecimal representation of RGB-values.")
            
        r = int(hex_string[:2], 16)
        g = int(hex_string[2:4], 16)
        b = int(hex_string[4:], 16)
        
        return r, g, b