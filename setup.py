from setuptools import setup, find_packages

setup(
    name='pyclc',
    version='0.1.0',
    description='A Python package for calculating',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Leo Araya',
    url='https://www.github.com/leoarayav/pyclc',
    license='MIT',
    packages=find_packages(),
    keywords=['pyclc', 'python', 'calculator', 'maths', 'physics', 'astrology', 'package'],
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