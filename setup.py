from setuptools import setup, find_packages
setup(
    name='bioModels_cache',
    version='0.1.0', 
    author='Brigit Parrish',
    author_email='briggit@uw.edu',
    description='A CLI tool to cache BioModels for Sys-Bio Projects', 
    url='https://github.com/sys-bio/BiomodelsCache',
    packages=find_packages(where='src'), 
    install_requires=[
        'biomodels_restful_api_client ==0.1.1',
    ],
    entry_points={
    },
)
