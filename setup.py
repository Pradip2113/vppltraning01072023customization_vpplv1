from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customization_vpplv1/__init__.py
from customization_vpplv1 import __version__ as version

setup(
	name="customization_vpplv1",
	version=version,
	description="customization_vpplv1",
	author="Quantbit",
	author_email="21pradipjadhav@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
