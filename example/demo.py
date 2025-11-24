import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.brightness_comparer import BrightnessComparer
from src.color_factory import ColorFactory

def main() -> None:
    '''Demonstration of how the brightness comparison works.
    
    Note: In both cases, the brightest color should be #FFFFFF.
    '''

    #Example for using a hex-list
    print('Getting the brightest color from a hex-list:')
    hex_list = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
    colors = ColorFactory.from_hex_list(hex_list)
    BrightnessComparer.print_brightest_color(colors)

    #Example for using the CSS colors API
    print('Getting the brightest color from the CSS colors API:')
    url = "https://csscolorsapi.com/api/colors"
    colors = ColorFactory.from_css_colors_api(url)
    BrightnessComparer.print_brightest_color(colors)

if __name__ == "__main__":
    main()