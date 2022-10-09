from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'String distance metrics'
LONG_DESCRIPTION = 'String distance metrics based on Levenshtein and Qwerty Matrix Distance'

# Setting up
setup(
        name="QLev", 
        version=VERSION,
        author="Alysson Amaral",
        author_email="alysson.amaral@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy'],
        keywords=['python', 'levenshtein', 'qwerty'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: String Classifier",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)