from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT = '-e .'

'''
requirements.txt—This file is used by pip to install all of the dependencies for your application.
 In this case, it contains only -e . This tells pip to install the requirements specified in setup.py. 
 It also tells pip to run
So it tells pip to install the requirements specified in setup.py.
'''
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='MLproject',
    version='0.0.1',
    description='My project',
    author='Youssef',
    author_email='ibnezzynyoussef@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)