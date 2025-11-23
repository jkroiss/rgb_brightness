from typing import List
from src.color import Color

class BrightnessComparer:
    '''
    Finds the highest brightness of Color-objects in a List.

    Additionally, it provides functionality to print the brightest color directly and 
    to format the found object into a proper human-readable string, if so desired.
    '''

    @staticmethod
    def get_brightest_color(colors: List[Color]):
        
        if not colors:
            raise ValueError("No list of colors provided.")

        return max(colors, key=lambda color: color.get_brightness())

    @staticmethod
    def format_brightest_color(color: Color) -> str:
        hex_string = color.hex_string
        if not hex_string.startswith('#'):
            hex_string = '#' + hex_string
        result = f'The brightest color is: {hex_string.upper()} (r={color.r}, g={color.g}, b={color.b})'
        if color.name:
            result += f', called "{color.name}"'
        return result
        
        
    @staticmethod
    def print_brightest_color(colors):
        brightest = BrightnessComparer.get_brightest_color(colors)
        output = BrightnessComparer.format_brightest_color(brightest)
        print(output)