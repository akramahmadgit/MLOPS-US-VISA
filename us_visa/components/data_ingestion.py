import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataInjestionArtifact

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataInjestionArtifact
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.data_access.usvisa_data import USvisaData


class DataInjestion:
    def __init__(self, data_injestion_config:DataIngestionConfig=DataIngestionConfig()) -> None:

        try:
            self.data_injestion_config = data_injestion_config
        except Exception as e:
            raise USvisaException(e, sys)
        