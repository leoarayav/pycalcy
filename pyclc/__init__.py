'''
    ### PyCLC - Python Calculations
    A lightweight library is a collection of overall methods calculations used in
    multiples areas, contains all methods done, where you can use it in your projects or simply
    to learn how to calculate something, this library is open source and free to use

    Project author and maintainer:
        Leo Araya (https://www.github.com/leoarayav)
'''

from .general import General
from .maths import Math
from .geometry import Geometry
from .physics import Physics
from .astrology import Astrology
from .crypt import Encrypt
from .__main__ import App

__title__ = "pyclc"
__version__ = "0.0.1"
__author__ = "Leo Araya"
__all__ = ['General', 'Math', 'Geometry', 'Physics', 'Astrology', 'Encrypt']