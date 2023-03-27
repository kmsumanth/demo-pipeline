from setuptools import setup,find_packages

setup(
    name="census-income",
    version="0.0.1",
    author="sumanth",
    author_email="kmsumanth002@gmail.com",
    packages=find_packages(),
    install_requirements=["pandas","numpy","flask"]
)