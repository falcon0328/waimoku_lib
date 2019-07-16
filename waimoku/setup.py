from setuptools import setup
from setuptools import find_packages
setup(
    name='waimoku',
    version='0.0.1',
    description='PythonScript to convert "Waimoku" participant information into "Yahoo! LODGE" participant list file format',
    author='Atsuki Seo',
    install_requires=["pandas", "openpyxl"],
    package_data={
        "waimoku": ["res/*.xlsx"]
    },
)
