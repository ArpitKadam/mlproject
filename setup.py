from setuptools import find_packages, setup

def get_requirements(filename: str) -> list:
    with open(filename, "r") as f:
        requirements = f.read().splitlines()
        E_DOT = '-e .' 
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "ArpitKadam",
    author_email="arpitkadam922@gmail.com",
    packages=find_packages(),
    license="MIT",
    install_requires= get_requirements("requirements.txt")
)