from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Data Structures',
    version='0.1',
    description='Implementation of common data structures',
    long_description=readme,
    author='Nicholas Schafran',
    author_email='nickschafran@fastmail.fm',
    url='https://github.com/nickschafran/data-structures',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

