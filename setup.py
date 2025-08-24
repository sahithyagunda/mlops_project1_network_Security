"""
Setup.py file is an essential part of packaging and distributing python projects. it is used by setup tools(or distutils in older python versions) to define configurations of your projects, such as its meta data, dependencies and more

"""

## find packages --- finds the folders with __init__.py and considers it has a package

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement) 
    except FileNotFoundError:
        print('File not found')
    return requirement_list


print(get_requirements())