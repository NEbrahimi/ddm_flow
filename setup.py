from setuptools import setup, find_packages

setup(
    name="ddm-flow",
    version="0.1",
    packages=find_packages(),

    install_requires=[
        'contourpy>=1.1.0',
        'matplotlib>=3.7.2',
        'numpy>=1.25.2',
        'openpyxl>=3.1.2',
        'packaging>=23.1',
        'pandas>=2.0.3',
        'Pillow>=10.0.0',
        'python-dateutil>=2.8.2',
        'pytz>=2023.3',
        'tzdata>=2023.3'
    ],

    author="Naz Ebrahimi",
    description="A toolset for processing, organizing, and visualizing data for individual FoVs from DDm analysis."
)
