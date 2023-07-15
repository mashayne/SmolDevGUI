from setuptools import setup, find_packages

setup(
    name='Smol Developer',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
    ],
    package_data={
        'smol_developer': ['assets/*'],
    },
    entry_points={
        'console_scripts': [
            'smol_developer=smol_developer.main:main',
        ],
    },
)