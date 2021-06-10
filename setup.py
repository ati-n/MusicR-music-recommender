from setuptools import setup, find_packages

setup(
    name="musicr",
    version="0.1.0",
    packages=find_packages(exclude="tests"),
    entry_points={
        "console_scripts": [
            "musicr = src.__main__:main"
        ]
    },
)

