from setuptools import setup, find_packages
from src import __author__, __version__, __license__

setup(
    name='pDrive',
    version=__version__,
    description='easy uploader for google drive',
    license=__license__,
    author=__author__,
    author_email='smatsumori[at]ailab.ics.keio.ac.jp',
    url='https://github.com/smatsumori/pDrive.git',
    keywords='python googledrive',
    packages=find_packages(),
    install_requires=['google-api-python-client'],
)
