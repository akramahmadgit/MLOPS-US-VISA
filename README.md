# MLOPS-US-VISA

## US VISA approval prediction project

### Lifecycle of Machine Learning Project
    1. Understanding the problem statement
    2. Data collection
    3. Exploratory data analysis
    4. Data cleaning
    5. Data pre processing
    6. Model training
    7. Choosing best model
    8. 


    

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

# mongo db setup
    install driver
        python -m pip install "pymongo[srv]"==3.6

# full code sample
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://visaproject:<password>@cluster0.fldzbco.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Note 
To save data in mongodb first we have to convert in dictionARY FORMAT
use pandas converter ---- to_dict

# define Data connection variables





# Data pre-processing and Feature Engineering
