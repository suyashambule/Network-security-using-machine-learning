from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
import os 
import sys
import pandas as pd
import numpy as np
from typing import List
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
import pymongo

load_dotenv()
MONGO_DB_URI=os.getenv('MONOGO_DB_URI')


class DataIngestion():
    def __init___(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config

            pass
        except Exception as e:
            raise NetworkSecurityException(e)
        
    def export_collection_as_df(self):
        try:
            database=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URI)
            collection=self.mongo_client[database][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df.drop(columns=['_id'],axis=1)         
        except Exception as e:
            raise NetworkSecurityException(e)



    def __init__(self):
        try:
            dataframe=self.export_collection_as_df()
        except Exception as e:
            raise NetworkSecurityException(e)



