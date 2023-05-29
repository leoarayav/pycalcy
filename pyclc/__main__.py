"""
This module is the main module of the package and contains the App class
"""

from typing import Callable, Any

class App:
    """This class contains methods for calculating"""

    def calculate(self, method: Callable[..., Any], *args) -> None:
        """
        This method calculates the result of the method passed as an argument

        Args:
            method (Callable): method to execute
            *args: arguments for the method
        
        Returns:
            float: result of the method
        """
        return method(*args)