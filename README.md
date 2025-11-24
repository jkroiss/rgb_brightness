# RGB Brightness

A little application to find the brightest color in a collection of colors represented as hexadecimal values.

## Description

This projects demonstrates:
- OOP principles
- Working with the Python standard library
- Testing code using unittest

Formula used for brightness calculation: sqrt(0.241 * R^2 + 0.691 * G^2 + 0.068 * B^2) 

## Installation
```bash
git clone https://github.com/jkroiss/rgb_brightness.git
cd rgb_brightness
```

**Note:** Since only the Python standard library is used, no `pip install -r requirements.txt` is required.

## Usage
```python
from src.brightness_comparer import BrightnessComparer
from src.color_factory import ColorFactory

hex_list = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
colors = ColorFactory.from_hex_list(hex_list)
BrightnessComparer.print_brightest_color(colors)
````

## Run demo
Make sure that the current directory is the root directory.

```bash
python examples/demo.py
````

## Run tests
Make sure that the current directory is the root directory.

```bash
python -m unittest 
```

## Requirements
Python 3.8+, no additional external dependencies
