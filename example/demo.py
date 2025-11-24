import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.brightness_comparer import BrightnessComparer
from src.color_factory import ColorFactory

def main() -> None:
    """Demonstration of how the brightness comparison works."""

    print('\n' + '=' * 80 + '\n')

    # Example for using a hex-list
    print('Getting the brightest color from a hex-list:')
    hex_list = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
    colors = ColorFactory.from_hex_list(hex_list)
    BrightnessComparer.print_brightest_color(colors)
    print('\n' + '=' * 80 + '\n')

    # Example for using the CSS colors API
    print('Getting the brightest color from all the colors from the CSS Colors API:')
    url = "https://csscolorsapi.com/api/colors"
    try:
        colors = ColorFactory.from_css_colors_api(url)
        BrightnessComparer.print_brightest_color(colors)
    except ValueError as e:
        print(f"Could not retrieve colors from the API: {e}")
    print('\n' + '=' * 80 + '\n')

    # Example for using the CSS colors API and only retrieving the blue colors
    print('Getting the brightest color from a group from the CSS Colors API:')
    url = "https://csscolorsapi.com/api/colors/group/blue"
    try:
        colors = ColorFactory.from_css_colors_api(url)
        BrightnessComparer.print_brightest_color(colors)
    except ValueError as e:
        print(f"Could not retrieve colors from the API: {e}")
    print('\n' + '=' * 80 + '\n')

    # Example for using the CSS colors API and only retrieving a single color
    print('Getting a single color from the CSS Colors API:')
    url = "https://csscolorsapi.com/api/colors/CadetBlue"
    try:
        colors = ColorFactory.from_css_colors_api(url)
        BrightnessComparer.print_brightest_color(colors)
    except ValueError as e:
        print(f"Could not retrieve colors from the API: {e}")
    print('\n' + '=' * 80 + '\n')

    # Example for using the CSS colors API and only retrieving the dark colors
    print('Getting the brightest color from a theme from the CSS Colors API:')
    url = "https://csscolorsapi.com/api/colors/theme/dark"
    try:
        colors = ColorFactory.from_css_colors_api(url)
        BrightnessComparer.print_brightest_color(colors)
    except ValueError as e:
        print(f"Could not retrieve colors from the API: {e}")
    print('\n' + '=' * 80 + '\n')

if __name__ == "__main__":
    main()