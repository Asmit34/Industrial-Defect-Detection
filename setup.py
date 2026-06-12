from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return list of requirements from a requirements.txt file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # removes \n and spaces

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="industrial_safety_monitoring",
    version="0.0.1",
    author="Asmit Oli",
    author_email="oliasmit272@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)