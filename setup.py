from setuptools import setup, find_packages  # type:ignore

with open("data_expectations/version.py", "r") as v:
    vers = v.read()
exec(vers)  # nosec

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r") as rm:
    long_description = rm.read()

setup(
    name="dataexpectations",
    version=__version__,
    description="Is your data meeting all your expecations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Joocer",
    packages=find_packages(include=["data_expectations", "data_expectations.*"]),
    url="https://github.com/joocer/data_expectations",
    install_requires=required,
)
