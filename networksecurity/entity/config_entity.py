from datetime import datetime
import os
from networksecurity.constant import training_pipeline

print(training_pipeline.PIPELINE_NAME)


class TrainingPipelineConfig:
    def __init__(self,time_stamp=datetime.now()):
        time_stamp=time_stamp.strftime()
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.Artifact_DIR
        self.artifact_dir=os.path.join(self.artifact_name,time_stamp)
        self.timestamp:str=time_stamp


class DATAINGESTIONCONFIG:
    def __init__(self,training_pipeline_config):
        self.data_ingestion:str=os.path(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
        )