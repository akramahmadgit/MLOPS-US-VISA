import os,


from us_visa.constant import *
from dataclass import dataclass
from datetime import datetime

TIMESTAMP : str = datetime.now().strftime("%m-%d-%Y %H:%M:%S")

#   create a data class 
@dataclass
class TrainingPipeLineConfig:
    pipeline_name : str = PIPELINE_NAME
    artifact_dir : str = os.path.join(ARTIFACT_DIR,TIMESTAMP)
    timestamp : str = TIMESTAMP


training_pipe_line_config : TrainingPipeLineConfig = TrainingPipeLineConfig()
    
