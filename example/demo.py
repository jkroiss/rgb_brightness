import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.brightness_comparer import BrightnessComparer
from src.color_factory import ColorFactory
from src.color import Color

def main():

    pass

if __name__ == "__main__":
    main()