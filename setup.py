from pathlib import Path

from setuptools import setup, find_packages
from pyqgis_package import __version__

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pyqgis_package",
    version=__version__,
    description="Template for PyQgis package.",
    long_description=long_description,
    url="https://github.com/robertohuru/pyqgis-package",
    author="Roberto Ohuru",
    author_email="robertohuru@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: GIS",
        "OSI Approved :: GNU General Public License (GPL)"
        "Programming Language :: Python :: 3.10",
    ],
    keywords="python package qgis",
    packages=find_packages(
        exclude=[
            "tests", "tests.*", "docker-compose.yml",
            "test_suite.py", "scripts", "scripts.*",
        ]),
    package_data={"pyqgis_package": ["version.json", "data/**"]},
    include_package_data=True,
    install_requires=[],
    extras_require={
        "dev": [],
        "test": [],
    },
)