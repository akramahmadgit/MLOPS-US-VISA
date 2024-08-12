import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.components.data_injestion import DataInjestion
'''
'from us_visa.components.data_validation import DataValidation
'from us_visa.components.data_transformation import DataTransformation
'from us_visa.components.model_trainer import ModelTrainer
'''
from us_visa.entity.config_entity import DataInjestionConfig
'''    
                                         DataValidationConfig,
                                         DataTransformationConfig,
                                         ModelTrainerConfig)
'''

from us_visa.entity.artifact_entity import DataInjestionArtifact
'''
,
                                            DataValidationArtifact,
                                            DataTransformationArtifact,
                                            ModelTrainerArtifact)
'''


class TrainingPipeline:

    def __init__(self):
        self.data_injestion_config = DataInjestionConfig()
        



    def start_data_injestion(self) -> DataInjestionArtifact:

        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_injestion = DataInjestion(data_injestion_config=self.data_injestion_config)
            data_injestion_artifact = data_injestion.initiate_data_injestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_injestion_artifact
        except Exception as e:
            raise USvisaException(e, sys)


    def run_pipeline(self,) -> None:

        try:
            data_injestion_artifact = self.start_data_injestion()
        except Exception as e:
            raise USvisaException(e, sys) from e
    

    
    