import os
import sys
import numpy as np
import pandas as pd


TARGET_COLUMNS="Result"
PIPELINE_NAME:str='NetworkSecurity'
Artifact_DIR:str='Artifacts'
file_name:str="phisingData.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"






DATA_INGESTION_COLLECTION_NAME:str = "Network data"
DATA_INGESTION_DATABASE_NAME:str='suyashambule'
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_FEATURE_STORE_DIR:str='feature_store'
DATA_INGESTION_DIR:str="ingested"   
DATA_INGESTION_TRAIN_TEST_SPILT:float=0.2