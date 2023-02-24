from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in amrita_neonet/__init__.py
from amrita_neonet import __version__ as version

setup(
	name="amrita_neonet",
	version=version,
	description="Preemie db",
	author="ICTS",
	author_email="nicu@aims.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
