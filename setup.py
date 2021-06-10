from setuptools import setup

setup(
    name="musicr",
    version="0.1.0",
    packages=["musicr"],
    entry_points={
        "console_scripts": [
            "musicr = src.__main__:main"
        ]
    },
)