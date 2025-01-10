from security.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from security.entity.config_entity import DataValidationConfig
from security.logging.logger import logging
from security.exception.exception import NetworkSecurityException
from security.constant.training_pipeline import SCHEMA_FILE_PATH
import pandas as pd
import os,sys
from security.utils.main_utils.utils import read_yaml_file
class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        