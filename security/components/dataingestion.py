from security.exception.exception import NetworkSecurityException
from security.logging.logger import logging
from security.entity.config_entity import DataIngestionConfig
import os 
import sys
import pandas as pd
import numpy as np
from typing import List
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
import pymongo

load_dotenv()
MONGO_DB_URI = os.getenv('MONGO_DB_URI')  # Fixed typo

class DataIngestion():
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            # Initialize mongo client once
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)
        except Exception as e:
            raise NetworkSecurityException(e)
        
    def export_collection_as_df(self):
        try:
            # Fetch database and collection name
            database = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            collection = self.mongo_client[database][collection_name]
            
            # Convert MongoDB collection to DataFrame
            df = pd.DataFrame(list(collection.find()))
            
            # Drop the '_id' column if it exists
            if "_id" in df.columns.to_list():
                df.drop(columns=['_id'], axis=1, inplace=True)
            
            # Return the dataframe
            return df
        
        except Exception as e:
            raise NetworkSecurityException(e)
    
    def ingest_data(self):
        try:
            # Get the data from MongoDB
            dataframe = self.export_collection_as_df()
            # You can process or use dataframe here
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e)