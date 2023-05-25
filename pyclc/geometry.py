"""
This module contains global calculations in geometry and most used of them
"""

from typing import Union

class Geometry:
    """This class contains methods for geometry calculations"""
    def geometric_progression(self, a: int | float, r: int | float, n: int) -> Union[int, float]:
        """
        This method calculates the geometric progression

        Args:
            a (int | float): The a
            r (int | float): The r
            n (int): The n

        Returns:
            int | float: The geometric progression
        """
        return a * r ** (n - 1)

    def hipotenuse(self, a: int | float, b: int | float) -> Union[int, float]:
        """
        This method calculates the hipotenuse

        Args:
            a (int | float): The a
            b (int | float): The b

        Returns:
            int | float: The hipotenuse
        """
        return (a ** 2 + b ** 2) ** 0.5
    
    def area(self, base: int | float, height: int | float) -> Union[int, float]:
        """
        This method calculates the area

        Args:
            base (int | float): The base
            height (int | float): The height

        Returns:
            int | float: The area
        """
        return base * height / 2
    
    def perimeter(self, a: int | float, b: int | float, c: int | float) -> Union[int, float]:
        """
        This method calculates the perimeter

        Args:
            a (int | float): The a
            b (int | float): The b
            c (int | float): The c

        Returns:
            int | float: The perimeter
        """
        return a + b + c
    
    def volume(self, base: int | float, height: int | float) -> Union[int, float]:
        """
        This method calculates the volume

        Args:
            base (int | float): The base
            height (int | float): The height

        Returns:
            int | float: The volume
        """
        return base * height
    
    def area_of_circle(self, radius: int | float) -> Union[int, float]:
        """
        This method calculates the area of circle

        Args:
            radius (int | float): The radius

        Returns:
            int | float: The area of circle
        """
        return 3.14 * radius ** 2
    
    def perimeter_of_circle(self, radius: int | float) -> Union[int, float]:
        """
        This method calculates the perimeter of circle

        Args:
            radius (int | float): The radius

        Returns:
            int | float: The perimeter of circle
        """
        return 2 * 3.14 * radius
    
    def volume_of_sphere(self, radius: int | float) -> Union[int, float]:
        """
        This method calculates the volume of sphere

        Args:
            radius (int | float): The radius

        Returns:
            int | float: The volume of sphere
        """
        return 4 / 3 * 3.14 * radius ** 3
    
    def area_of_sphere(self, radius: int | float) -> Union[int, float]:
        """
        This method calculates the area of sphere

        Args:
            radius (int | float): The radius

        Returns:
            int | float: The area of sphere
        """
        return 4 * 3.14 * radius ** 2
    
    def triangle_area(self, a: int | float, b: int | float, c: int | float) -> Union[int, float]:
        """
        This method calculates the triangle area

        Args:
            a (int | float): The a
            b (int | float): The b
            c (int | float): The c

        Returns:
            int | float: The triangle area
        """
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    
    def polygon_area(self, perimeter: int | float, apothem: int | float) -> Union[int, float]:
        """
        This method calculates the polygon area

        Args:
            perimeter (int | float): The perimeter
            apothem (int | float): The apothem

        Returns:
            int | float: The polygon area
        """
        return perimeter * apothem / 2