"""
This module contains global calculations and most used of them
"""

from typing import List, Tuple

_numbers = List[int]

class Typical:
    """The Global class who contains overall methods calculations"""

    def get_average(self, data: _numbers) -> float:
        """
        This method calculates the average of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            float: The average
        """
        return sum(data) / len(data)

    def get_variance(self, data: _numbers) -> float:
        """
        This method calculates the variance of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            float: The variance
        """
        average = self.get_average(data)
        return sum([(i - average) ** 2 for i in data]) / len(data)

    def get_standard_deviation(self, data: _numbers) -> float:
        """
        This method calculates the standard deviation of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            float: The standard deviation
        """
        return self.get_variance(data) ** 0.5

    def get_coefficient_of_variation(self, data: _numbers):
        """
        This method calculates the coefficient of variation of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            float: The coefficient of variation
        """
        return self.get_standard_deviation(data) / self.get_average(data)

    def get_percentile(self, data: _numbers, percentile: float) -> float:
        """
        This method calculates the percentile of a list

        Args:
            data (_numbers): The list of data
            percentile (float): The percentile
        
        Returns:
            float: The percentile
        """
        data.sort()
        index = (len(data) - 1) * percentile
        floor = int(index)
        ceil = floor + 1
        return data[floor] + (data[ceil] - data[floor]) * (index - floor)

    def get_median(self, data: _numbers) -> float:
        """
        This method calculates the median of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            float: The median
        """
        return self.get_percentile(data, 0.5)

    def get_quartile(self, data: _numbers) -> Tuple[float, float]:
        """
        This method calculates the quartile of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            tuple[float, float]: The quartile
        """
        return self.get_percentile(data, 0.25), self.get_percentile(data, 0.75)

    def get_interquartile_range(self, data: _numbers) -> float:
        """
        This method calculates the interquartile range of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            float: The interquartile range
        """
        return self.get_quartile(data)[1] - self.get_quartile(data)[0]

    def get_outliers(self, data: _numbers) -> List[float]:
        """
        This method calculates the outliers of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            list[float]: The list of outliers
        """
        interquartile_range = self.get_interquartile_range(data)
        quartile = self.get_quartile(data)
        return [i for i in data if i < quartile[0] - 1.5 \
                 * interquartile_range or i > quartile[1] + 1.5 * interquartile_range]

    def get_outliers_removed(self, data: _numbers) -> List[float]:
        """
        This method calculates the outliers removed of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            list[float]: The list of outliers removed
        """
        outliers = self.get_outliers(data)
        return [i for i in data if i not in outliers]

    def binarization(self, data: _numbers) -> List[int]:
        """
        This method calculates the binarization of a list

        Args:
            data (_numbers): The list of data
        
        Returns:
            list[int]: The list of binarization
        """
        average = self.get_average(data)
        return [1 if i > average else 0 for i in data]
    
    def imc(self, weight: float, height: float) -> float:
        """
        This method calculates the IMC (Body Mass Index)

        Args:
            weight (float): The weight
            height (float): The height
        
        Returns:
            float: The IMC
        """
        return weight / height ** 2