'''
    This is a simple example of how to use pyclc
    Scenario: "Using pyclc to calculate and use the astrological methods 🪐"
    Author: Leo Araya (https://www.github.com/leoarayav)
'''

# Import the main class and the Astrology class :)
from pyclc import App, Astrology

# Create an instance of the main class who contains the calculate method
pycalc = App()

# Create an instance of the Astrology class
astro = Astrology()

# Calculate light year
print(pycalc.calculate(astro.light_year, 1e+15))

# Expected output: 0.1056970721911003