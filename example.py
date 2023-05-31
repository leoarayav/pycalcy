'''
    This is a simple example of how to use pyclc
    Scenario: "Using pyclc to calculate and use the astrological methods 🪐"
    Author: Leo Araya (https://www.github.com/leoarayav)
'''

# Import the main class and the Astrology class :)
from pyclc import App, Astrology

# Create an instance of the App class
app = App()

# Create an instance of the Astrology class
astro = Astrology()

tst = app(astro.astronomical_unit, 2)

# Print the result
print(tst)