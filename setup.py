from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "openai",  # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'mypackage-doc = mypackage.autodoc:generate_documentation',
            'mypackage-readme = mypackage.autodoc:generate_readme',
            'mypackage-offline = mypackage.thirdparty:main'
        ],
    },
)
