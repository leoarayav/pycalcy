from typing import Callable

class App:
    """This class contains methods for calculating"""
    def calculate(self, method: Callable, *args) -> float:
        return method(*args)