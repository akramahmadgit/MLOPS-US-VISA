import os
from datetime import datetime


# Define a variable for project name
DATABASE_NAME = 'db_usvisa'
COLLECTION_NAME = 'col_usvisa'
MONGODB_URL_KEY = 'MONGODB_URL'

# Define pipeline name and artifact directory
PIPELINE_NAME : str = 'pl_usvisa'
ARTIFACT_DIR : str = 'artifact'



# Data injestion related constants
DATA_INJESTION_COLLECTION_NAME : str = 'col_usvisa'
DATA_INJESTION_DIR_NAME : str = 'data_injestion'
DATA_INJESTION_FEATURE_STORE_DIR : str = 'feature_store'
DATA_INJESTION_INJESTED_DIR : str = 'injested'
DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2


# model creating files
TRAIN_FILE_NAME : str = 'train.csv'
TEST_FILE_NAME : str = 'test.csv'

# Define model file name
FILE_NAME : str = 'us_visa.csv'
MODEL_FILE_NAME = 'model.pkl'



