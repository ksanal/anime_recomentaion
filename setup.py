from setuptools import setup, find_packages

with open("requirments.txt") as f:
    requirements = f.read().splitlines()


setup(
    name='MLOPS-PROJECT-3',
    version='0.1',
    author='Sanal',
    packages=find_packages(),
    install_requires=requirements,
)