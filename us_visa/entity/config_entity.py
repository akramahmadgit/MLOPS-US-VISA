import os


from us_visa.constant import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP : str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

#   create a data class 
@dataclass
class TrainingPipeLineConfig:
    pipeline_name : str = PIPELINE_NAME
    artifact_dir : str = os.path.join(ARTIFACT_DIR,TIMESTAMP)
    timestamp : str = TIMESTAMP


training_pipeline_config : TrainingPipeLineConfig = TrainingPipeLineConfig()
    

@dataclass
class DataInjestionConfig:
    data_injestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INJESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_injestion_dir, DATA_INJESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_injestion_dir, DATA_INJESTION_INJESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_injestion_dir, DATA_INJESTION_INJESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INJESTION_COLLECTION_NAME





