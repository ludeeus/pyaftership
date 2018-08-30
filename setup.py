"""Setup"""
import setuptools
with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="pyaftership",
    version="0.0.4",
    author="Joakim Sorensen @ludeeus",
    author_email="ludeeus@gmail.com",
    description="A module to get information pending parcels.",
    long_description=LONG,
    install_requires=['requests'],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/pyaftership",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
