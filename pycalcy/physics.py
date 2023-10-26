"""
This module contains global calculations in physics and most used of them
"""

from typing import Union

class Physics:
    """This class contains methods for physics calculations"""

    def velocity(self, distance: Union[int, float], time: Union[int, float]) -> float:
        """
        Calculate velocity using distance and time

        Args:
            distance (Union[int, float]): Distance traveled
            time (Union[int, float]): Time taken to travel
        
        Returns:
            Union[int, float]: Velocity
        """
        return distance / time
    
    def acceleration(self, velocity: Union[int, float], time: Union[int, float]) -> float:
        """
        Calculate acceleration using velocity and time

        Args:
            velocity (Union[int, float]): Velocity
            time (Union[int, float]): Time taken to travel
        
        Returns:
            Union[int, float]: Acceleration
        """
        return velocity / time
    
    def distance(self, velocity: Union[int, float], time: Union[int, float]) -> float:
        """
        Calculate distance using velocity and time

        Args:
            velocity (Union[int, float]): Velocity
            time (Union[int, float]): Time taken to travel
        
        Returns:
            Union[int, float]: Distance
        """
        return velocity * time
    
    def time(self, distance: Union[int, float], velocity: Union[int, float]) -> float:
        """
        Calculate time using distance and velocity

        Args:
            distance (Union[int, float]): Distance traveled
            velocity (Union[int, float]): Velocity
        
        Returns:
            Union[int, float]: Time taken to travel
        """
        return distance / velocity
    
    def force(self, mass: Union[int, float], acceleration: Union[int, float]) -> float:
        """
        Calculate force using mass and acceleration

        Args:
            mass (Union[int, float]): Mass of object
            acceleration (Union[int, float]): Acceleration of object
        
        Returns:
            Union[int, float]: Force
        """
        return mass * acceleration
    
    def density(self, mass: Union[int, float], volume: Union[int, float]) -> float:
        """
        Calculate density using mass and volume

        Args:
            mass (Union[int, float]): Mass of object
            volume (Union[int, float]): Volume of object
        
        Returns:
            Union[int, float]: Density
        """
        return mass / volume
    
    def pressure(self, force: Union[int, float], area: Union[int, float]) -> float:
        """
        Calculate pressure using force and area

        Args:
            force (Union[int, float]): Force
            area (Union[int, float]): Area
        
        Returns:
            Union[int, float]: Pressure
        """
        return force / area
        
    def period(self, frequency: Union[int, float]) -> float | int:
        """
        Calculate period using frequency

        Args:
            frequency (Union[int, float]): Frequency
        
        Returns:
            Union[int, float]: Period
        """
        return 1 / frequency

    def frequency(self, period: Union[int, float]) -> float | int:
        """
        Calculate frequency using period

        Args:
            period (Union[int, float]): Period of wave
        
        Returns:
            Union[int, float]: Frequency
        """
        if period == 0:
            return 0
        return 1 / period | 0