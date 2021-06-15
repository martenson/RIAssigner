#!/usr/bin/env python
import os
from setuptools import find_packages
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(here, "RIAssigner", "__version__.py")) as f:
    exec(f.read(), version)

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="RIAssigner",
    version=version["__version__"],
    description="Python library for retention index calculation.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="RECETOX",
    author_email="helge.hecht@recetox.muni.cz",
    url="https://github.com/hechth/RIAssigner",
    packages=find_packages(exclude=['*tests*']),
    license="MIT License",
    zip_safe=False,
    keywords=[
        "gas chromatography",
        "mass spectrometry",
        "retention index"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    test_suite="tests",
    python_requires='>=3.7',
    install_requires=[
        "matchms",
        "numpy",
        "pandas",
        "pint"
    ],
    extras_require={},
)
