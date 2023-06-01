"""
This module is the main module of the package and contains the App class
"""

import typing as tp

class App:
    """This class contains methods for calculating"""

    def calculate(
            self, 
            method: tp.Callable[..., tp.Any], 
            *args: tp.Any
        ) -> None:
        """
        This method calculates the result of the method passed as an argument

        Args:
            method (Callable): method to execute
            *args: arguments for the method
        
        Returns:
            float: result of the method
        """
        return method(*args)
    
    def __repr__(self) -> str:
        """
        This method returns the representation string of the class

        Returns:
            str: string representation of the class
        """
        return f"{self.__class__.__name__}()"
    
    def __str__(self) -> str:
        """
        This method string of the class

        Returns:
            str: string representation of the class
        """
        return self.__repr__()
    
    def __call__(self, *args: tp.Any) -> None:
        """
        This method calculates the result of the method passed as an argument

        Args:
            *args: arguments for the method

        Returns:
            None
        """
        return self.calculate(*args)