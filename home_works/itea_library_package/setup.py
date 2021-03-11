from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='itea_library',
    version='1.0',
    packages=find_packages(),
    description='ITEA library home work',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
