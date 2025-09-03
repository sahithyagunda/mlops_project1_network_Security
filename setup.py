from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str = 'requirements.txt') -> List[str]:
    """
    Returns a list of requirement strings read from requirements.txt,
    excluding '-e .' or other invalid lines.
    """
    requirements = []
    try:
        with open(file_path) as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('-e'):
                    requirements.append(line)
    except FileNotFoundError:
        print("requirements.txt not found.")
    
    return requirements

setup(
    name="NetworkSecurityProject",
    version="0.0.1",
    author="Sahithya",
    author_email="gundasahithya908@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
