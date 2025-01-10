import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

ca=certifi.where()
load_dotenv()
MONGO_DB_URI=os.getenv("MONGO_DB_URI")

ca=certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def Insert_data_mango(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URI)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    file_path='/Users/suyash/Desktop/Network security project/Network_data/phisingData.csv'
    Database="suyashambule"
    collection="network data"
    network_obj=NetworkDataExtract()
    records=network_obj.csv_to_json(file_path=file_path)
    no_of_records=network_obj.Insert_data_mango(records,Database,collection)
    print(no_of_records)




        


        


