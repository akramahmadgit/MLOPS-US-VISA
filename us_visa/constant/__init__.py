import os
from datetime import date


# Define a variable for project name
DATABASE_NAME = 'db_usvisa'
COLLECTION_NAME = 'col_usvisa'
MONGODB_URL_KEY = 'MONGODB_URL'

# Define pipeline name and artifact directory
PIPELINE_NAME : str = 'pl_usvisa'
ARTIFACT_DIR : str = 'artifact'

# Define model file name
MODEL_FILE_NAME = 'model.pkl'

# Data injestion related constants
DATA_INJESTION_COLLECTION_NAME : str = 'visa_data'
DATA_INJESTION_DIR_NAME : str = 'data_injestion'
DATA_INJESTION_FEATURE_STORE_DIR : str = 'feature_store'
DATA_INJESTION__INJESTED_DIR : str = 'injested dir'
DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2
