from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ml-project',
    version='0.0.1',
    author='Atharva Kulkarni',
    author_email='kulkarni.atharva.18.05.2004@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)
