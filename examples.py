'''
    This is a simples examples of how to use pycalcy
    Author: Leo Araya (https://www.github.com/leoarayav)
'''

from pycalcy import (
    App,
    Geometry,
    Math,
    Typical,
    Physics,
    Astronomy,
    Encrypt
)

'''Initialize the class objects'''
pycalcy = App()

geometry = Geometry()
math = Math()
typical = Typical()
physics = Physics()
astronomy = Astronomy()
crypt = Encrypt()

'''This is a simple example of how to use pycalcy to calculate the area of a circle'''
aoc = pycalcy(geometry.area_of_circle, 6)
print(aoc)

'''This is a simple example of how to check the orbit of a planet'''
planet = pycalcy(astronomy.orbital_period, 7, 6)
print(planet)

'''This is a simple example of how to crypt a message to binary'''
message = pycalcy(crypt.encrypt_text_to_binary, 'Hello World')
print(message)

'''This is a simple example of how to calculate the interpolation of a list'''
itp = pycalcy(math.interpolation, [2, 5, 6, 9, 24], 6)
print(itp)

'''This is a simple example of how to calculate the density of a body'''
dsty = pycalcy(physics.density, 6, 7)
print(dsty)

'''This is a simple example of how to determinate the IMC of a person'''
val = pycalcy(typical.imc, 75, 1.70)
print(val)