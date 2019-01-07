# from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='aspea002_helloworld',
    version='0.1',
    description='Practice creating package for use with pip',
    author='Andrew Spear',
    author_email='porschelvr83@yahoo.com',
    zip_safe=False,
    url='https://github.com/prowler0305/simple_pip_install',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # packages=['helloworld']
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
