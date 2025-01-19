from setuptools import setup, find_packages

setup(
    name='topsis_abhinavraj_102217008',
    version='1.3',
    packages=find_packages(),
    install_requires=['numpy','pandas'],  # List your dependencies here
    long_description=open('README.md').read(),  # Automatically takes content from your README file
    long_description_content_type="text/markdown",
    description="Python implementation of the TOPSIS method for multi-criteria decision analysis",
   
    entry_points={
        'console_scripts': [
            'topsis = topsis.main:main',  # This connects the command `topsis` to `main()` function
        ],
    },
)