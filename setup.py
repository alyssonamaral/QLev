from setuptools import setup, find_packages
with open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

VERSION = '1.0.0' 
DESCRIPTION = 'String distance metrics based on Levenshtein and Qwerty Matrix Distance'

# Setting up
setup(
        name="QLev", 
        version=VERSION,
        author="Alysson Amaral",
        author_email="alysson.amaral@outlook.com",
        url="https://github.com/alyssonamaral/QLev",
        description=DESCRIPTION,
        long_description=readme,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=['numpy'],
        keywords=['python', 'levenshtein', 'qwerty'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
            "License :: OSI Approved :: MIT License",
        ]
)