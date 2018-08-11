"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='num2cyrillic',
    description='Python class for converting numbers into Bulgarian cyrillic words',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ClaimCompass/num2cyrillic',
    download_url='https://github.com/ClaimCompass/num2cyrillic',
    author='claimcompass.eu',
    author_email='info@claimcompass.eu',
    license='LGPLv3',
    test_suite="num2cyrillic.test_sample.test_all",
    version='1.0.0',
    py_modules=['num2cyrillic'],
    install_requires=[],
    entry_points={},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ),
)