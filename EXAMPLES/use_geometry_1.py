import sys
import alpha.mathlib.geometry as geometry  # find and run geometry.py
from alpha.mathlib import geometry
from alpha.mathlib.geometry import circle_area
import alpha
print(alpha.circle_area(10))
from alpha import *  # import mathlib and dbutil and net

# from ..foo import bar

#  module.name
print(f"{geometry.PI = }")

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")
print('-' * 60)
for path in sys.path:
    print(path)

# module search order
# 1. current folder
# 2. folders in PYTHONPATH env variable
# 3. *lib* folders under install folder