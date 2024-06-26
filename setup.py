"""Setup configuration."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Ludeeus",
    author_email="hi@ludeeus.dev",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Async Python wrapper for the AfterShip API.",
    install_requires=["aiohttp>=3.6.1,<4.0"],
    license="MIT license",
    long_description_content_type="text/markdown",
    long_description=readme,
    name="pyaftership",
    packages=find_packages(include=["pyaftership", "pyaftership.*"]),
    python_requires=">=3.12",
    url="https://github.com/ludeeus/pyaftership",
    version="main",
)
