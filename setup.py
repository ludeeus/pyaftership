"""Setup configuration."""
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Ludeeus",
    author_email="hi@ludeeus.dev",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="",
    install_requires=["aiohttp>=3.6.1,<4.0", "async_timeout"],
    license="MIT license",
    long_description_content_type="text/markdown",
    long_description=readme,
    name="pyaftership",
    packages=find_packages(include=["pyaftership", "pyaftership.*"]),
    url="https://github.com/ludeeus/pyaftership",
    version="master",
)
