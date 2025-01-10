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
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e)
        
    def start_data_validation(self)->DataValidationArtifact:
        try:
            train_file=self.data_ingestion_artifact.trained_file_path
            test_file=self.data_ingestion_artifact.test_file_path
            train_df=DataValidation.read_data(train_file)
            test_df=DataValidation.read_data(test_file)
        except Exception as e:
            raise NetworkSecurityException(e)
        
    def validation_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            no_of_colums=len(self._schema_config)
            logging.info(f'Required number os columns:{no_of_colums}')
            logging.info(f'Data frame columns:{len(dataframe.columns)}')
            if len(dataframe.columns)==no_of_colums:
                return True
            return False
        except Exception as e:
            raise NetworkSecurityException(e)
        
        