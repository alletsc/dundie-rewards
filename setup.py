import os

from setuptools import find_packages, setup


def read(*paths):
    ''' Read the content of a text file safely. '''
    root_path = os.path.dirname(__file__)
    filepath = os.path.join(root_path, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    ''' Read the content of the requirements file. '''
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git", '"', '-'))
    ]


setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Stella Costa",
    python_requires=">=3.8.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['dundie=dundie.__main__:main'],
    },
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements.dev.txt"),
        "test": read("requirements.test.txt")
    }
)
