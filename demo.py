
'''
from us_visa.logger import logging
from us_visa.exception import USvisaException

import sys

logging.info("You have successfully created a custom logging project")


try:
    a=5/0
except Exception as e:
    raise USvisaException(e, sys)
'''
from us_visa.pipeline.training_pipeline import TrainingPipeline

obj = TrainingPipeline()
obj.run_pipeline()

