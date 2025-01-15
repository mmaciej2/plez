from setuptools import find_packages, setup

__version__ = "0.1.0"

long_description = open("README.md").read()

install_requires = [
    "matplotlib",
]

setup(
    name="plez",
    version=__version__,
    author="Matt Maciejewski",
    author_email="matt@mmaciejewski.com",
    url="https://github.com/mmaciej2/plez",
    description="Plotting for LaTeX is EZ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=install_requires,
)
