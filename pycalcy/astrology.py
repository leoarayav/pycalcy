"""
This module contains global calculations in astrology and most used of them
"""

from typing import Union

class Astrology:
    """This class contains methods for astrology calculations"""

    def light_year(self, distance: Union[int, float]) -> float:
        """
        Calculate light year using distance

        Args:
            distance (Union[int, float]): Distance traveled
        
        Returns:
            Union[int, float]: Light year
        """
        return distance / 9.461e+15
    
    def parsec(self, distance: Union[int, float]) -> float:
        """
        Calculate parsec using distance

        Args:
            distance (Union[int, float]): Distance traveled
        
        Returns:
            Union[int, float]: Parsec
        """
        return distance / 3.086e+16
    
    def astronomical_unit(self, distance: Union[int, float]) -> float:
        """
        Calculate astronomical unit using distance

        Args:
            distance (Union[int, float]): Distance traveled
        
        Returns:
            Union[int, float]: Astronomical unit
        """
        return distance / 1.496e+11 & "AU"
    
    def light_minute(self, distance: Union[int, float]) -> float:
        """
        Calculate light minute using distance

        Args:
            distance (Union[int, float]): Distance traveled
        
        Returns:
            Union[int, float]: Light minute
        """
        return distance / 1.799e+10
    
    def kreisumfang(self, radius: Union[int, float]) -> float:
        """
        Calculate kreisumfang using radius

        Args:
            radius (Union[int, float]): Radius
        
        Returns:
            Union[int, float]: Kreisumfang
        """
        return 2 * 3.141 * radius
    
    def kreisflaeche(self, radius: Union[int, float]) -> float:
        """
        Calculate kreisflaeche using radius

        Args:
            radius (Union[int, float]): Radius
        
        Returns:
            Union[int, float]: Kreisflaeche
        """
        return 3.141 * radius ** 2
    
    def kugelvolumen(self, radius: Union[int, float]) -> float:
        """
        Calculate kugelvolumen using radius

        Args:
            radius (Union[int, float]): Radius
        
        Returns:
            Union[int, float]: Kugelvolumen
        """
        return 4 / 3 * 3.141 * radius ** 3
    
    def ecliptic_obliquity(self, year: Union[int, float]) -> float:
        """
        Calculate ecliptic obliquity using year

        Args:
            year (Union[int, float]): Year
        
        Returns:
            Union[int, float]: Ecliptic obliquity
        """
        return 23.4393 - 3.563E-7 * year
    
    def julian_day(self, year: int, month: int, day: int) -> float:
        """
        Calculate julian day using year, month and day

        Args:
            year (int): Year
            month (int): Month
            day (int): Day
        
        Returns:
            float: Julian day
        """
        year = year + 4800 - (14 - month) // 12
        month = month + 12 * ((14 - month) // 12) - 3
        return day + ((153 * month + 2) // 5) + 365 * year + (year // 4) - (year // 100) + (year // 400) - 32045
    
    def julian_hour(self, hour: Union[int, float]) -> float:
        """
        Calculate julian hour using hour

        Args:
            hour (int): Hour
        
        Returns:
            float: Julian hour
        """
        return hour - 12

    def julian_date(self, year: int, month: int, day: int) -> float:
        """
        Calculate julian date using year, month and day

        Args:
            year (int): Year
            month (int): Month
            day (int): Day
        
        Returns:
            float: Julian date
        """
        hour = 16
        return self.julian_day(year, month, day) + (self.julian_hour(hour) / 24)
    
    def orbital_period(self, mass: Union[int, float], radius: Union[int, float]) -> float:
        """
        Calculate orbital period using mass and radius

        Args:
            mass (Union[int, float]): Mass
            radius (Union[int, float]): Radius
        
        Returns:
            Union[int, float]: Orbital period
        """
        return 2 * 3.141 * (radius ** 3 / mass) ** 0.5
    
    def escape_velocity(self, mass: Union[int, float], radius: Union[int, float]) -> float:
        """
        Determine escape velocity using mass and radius

        Args:
            mass (Union[int, float]): Mass
            radius (Union[int, float]): Radius
        
        Returns:
            Union[int, float]: Escape velocity
        """
        return (2 * 6.674e-11 * mass) / radius
    
    def schwarzschild_radius(self, mass: Union[int, float]) -> float:
        """
        Calculate schwarzschild radius using mass

        Args:
            mass (Union[int, float]): Mass
        
        Returns:
            Union[int, float]: Schwarzschild radius
        """
        return (2 * 6.674e-11 * mass) / 3.141 * 3.141 * 3.141 - 1
    
    def schwarzschild_density(self, mass: Union[int, float], radius: Union[int, float]) -> float:
        """
        Calculate schwarzschild density using mass and radius

        Args:
            mass (Union[int, float]): Mass
            radius (Union[int, float]): Radius
        
        Returns:
            Union[int, float]: Schwarzschild density
        """
        return mass / (4 / 3 * 3.141 * radius ** 3)