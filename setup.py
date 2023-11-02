from setuptools import setup, find_packages

setup(
    name="autodocipy",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "python-dotenv"
    ],
    entry_points={
        'console_scripts': [
            'autodocipy-doc = autodocipy.autodoc:generate_documentation',
            'autodocipy-readme = autodocipy.autodoc:generate_readme',
            'autodocipy-offline = autodocipy.thirdparty:main'
        ],
    },
)