'''
    ### PyCLC - Python Calculations
    A lightweight library is a collection of overall methods calculations used in
    multiples areas, contains all methods done, where you can use it in your projects or simply
    to learn how to calculate something, this library is open source and free to use

    Project author and maintainer:
        Leo Araya (https://www.github.com/leoarayav)
'''

from .typical import Typical
from .maths import Math
from .geometry import Geometry
from .physics import Physics
from .astronomy import Astronomy
from .crypt import Encrypt
from .__main__ import App

__title__ = "pycalcy"
__version__ = "0.0.1"
__author__ = "Leo Araya"
__all__ = ['Typical', 'Math', 'Geometry', 'Physics', 'Astronomy', 'Encrypt']