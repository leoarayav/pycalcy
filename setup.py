from setuptools import setup, find_packages

setup(
    name='pycalcy',
    version='0.1.2',
    description='A pretty good globals calculation package for Python Development and more',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Leo Araya',
    url='https://www.github.com/leoarayav/pycalcy',
    license='MIT',
    packages=find_packages(),
    keywords=['pycalcy', 'python', 'calculator', 'maths', 'physics', 'astrology', 'package'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)