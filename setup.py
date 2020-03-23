""" Setup file for mkp
"""
import sys

from setuptools import setup, find_packages
from pkg_resources import VersionConflict, require

import mkp as mkp

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":
    setup(
        name=mkp.__title__,
        version=mkp.__version__,
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        packages=find_packages(exclude=["tests"]),
        install_requires=["click==7.1.1"],
        include_package_data=True,
        zip_safe=False,
        entry_points={"console_scripts": ["mkp=mkp.__main__:main"]},
        author=mkp.__author__,
        author_email=mkp.__author_email__,
        description=mkp.__description__,
        license=mkp.__license__,
        url=mkp.__url__,
    )
