# MLOPS-US-VISA

Installations
1. Git and GitHub
2. Anaconda
3. VS Code





# Create a new environment
    conda create -n env_visa python=3.11.5
    conda activate env_visa 
    
# Setup.py
add code to show us_visa_Project as installed package

    from setuptools import setup, find_packages
    setup(
        name=" us_visa_Project",
        version='0.0.0',
        description='Project for predicting US Visa approval',
        author='Akram Ahmad',
        author_email='akram.ahmad2009@gmail.com',
        packages=find_packages(),

    )

