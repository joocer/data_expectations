from setuptools import setup, find_packages  # type:ignore

with open("src/version.py", "r") as v:
    vers = v.read()
exec(vers)  # nosec

with open("README.md", "r") as rm:
    long_description = rm.read()

setup(
    name="data-expectations",
    version=__version__,
    description="Is your data meeting all your expecations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Joocer",
    packages=find_packages(include=["src", "src.*"]),
    url="https://github.com/joocer/data-expectations",
    install_requires=[],
)
