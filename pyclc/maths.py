"""
This module contains global calculations in mathematics and most used of them
"""

from typing import List, Union, Sequence

class Math:
    """The Math class who contains overall methods calculations"""

    def power(self, data: List[Union[int, float]], power: int) -> List[float]:
        """
        This method calculates the power of a list

        Args:
            data (_numbers): The list of data
            power (int): The power
        
        Returns:
            list[float]: The list of power
        """
        return [i ** power for i in data]

    def polynomial(self, data: List[Union[int, float]], x: int | float) -> int:
        """
        This method calculates the polynomial of a list

        Args:
            data (List[Union[int, float]]): The list of data
            x (int): The value of x

        Returns:
            int: The polynomial
        """
        return sum([i * x ** (len(data) - 1 - data.index(i)) for i in data])

    def interpolation(self, data: List[Union[int, float]], x: int | float) -> int:
        """
        This method calculates the interpolation of a list

        Args:
            data (List[Union[int, float]]): The list of data
            x (int): The value of x

        Returns:
            int: The interpolation
        """
        return sum([i * x ** data.index(i) for i in data])
    
    def interest(self, capital: int | float, rate: int, time: int) -> Union[int, float]:
        """
        This method calculates the interest

        Args:
            capital (int | float): The capital
            rate (int | float): The rate
            time (int | float): The time

        Returns:
            int | float: The interest
        """
        return capital * rate * time / 100
    
    def compound_interest(self, capital: int | float, rate: int, time: int) -> Union[int, float]:
        """
        This method calculates the compound interest

        Args:
            capital (int | float): The capital
            rate (int | float): The rate
            time (int | float): The time

        Returns:
            int | float: The compound interest
        """
        return capital * (1 + rate / 100) ** time
    
    def add_elements(self, data: Sequence[int | float]) -> Union[int, float]:
        """
        This method calculates the sum of elements

        Args:
            data (Sequence[int | float]): The sequence of data

        Returns:
            int | float: The sum of elements
        """
        return sum(data)
    
    def binomial_coefficient(self, n: int, k: int) -> int:
        """
        This method calculates the binomial coefficient

        Args:
            n (int): The n
            k (int): The k

        Returns:
            int: The binomial coefficient
        """
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))
    
    def factorial(self, n: int) -> int:
        """
        This method calculates the factorial

        Args:
            n (int): The n

        Returns:
            int: The factorial
        """
        return 1 if n == 0 else n * self.factorial(n - 1)
    
    def permutation(self, n: int, k: int) -> int:
        """
        This method calculates the permutation

        Args:
            n (int): The n
            k (int): The k

        Returns:
            int: The permutation
        """
        return self.factorial(n) / self.factorial(n - k)
    
    def combination(self, n: int, k: int) -> int:
        """
        This method calculates the combination

        Args:
            n (int): The n
            k (int): The k

        Returns:
            int: The combination
        """
        return self.permutation(n, k) / self.factorial(k)
    
    def arithmetic_progression(self, a: int | float, d: int | float, n: int) -> Union[int, float]:
        """
        This method calculates the arithmetic progression

        Args:
            a (int | float): The a
            d (int | float): The d
            n (int): The n

        Returns:
            int | float: The arithmetic progression
        """
        return a + (n - 1) * d
    
    def fibonacci(self, n: int) -> int:
        """
        This method calculates the fibonacci

        Args:
            n (int): The n

        Returns:
            int: The fibonacci
        """
        return n if n <= 1 else self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def power_series(self, x: int | float, n: int) -> int | float:
        """
        This method calculates the power series

        Args:
            x (int | float): The x
            n (int): The n

        Returns:
            int | float: The power series
        """
        return sum([x ** i for i in range(n + 1)])
    
    def derivative(self, data: List[Union[int, float]]) -> List[Union[int, float]]:
        """
        This method calculates the derivative

        Args:
            data (List[Union[int, float]]): The list of data

        Returns:
            List[Union[int, float]]: The derivative
        """
        return [i * data.index(i) for i in data]