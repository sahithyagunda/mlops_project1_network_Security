## this file talks about pushing data into mongodb
import os
import json
import sys
import certifi ##python package provides set of root certificates -- used to make secure http connection
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()
MONGO_DB_URI=os.getenv("MONGO_DB_URI")

ca=certifi.where() ## retrieves the path to the bundle of root ca(certificate authorities) certificates and store it in "ca" variable. ensures the server we are connceting to is authorized and safe.


class NetworkDataExtract():
    def __init__(self):
        try:  
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def csv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values()) ##converting data into json
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def insert_data_mongodb(self,records,database,collections): ## in mongodb we neeed to create database and collection-like a table in sql
        try:
            self.database = database
            self.collections = collections
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI) ## craeting client to connect with monogo db
            self.database = self.mongo_client[self.database]
            self.collections = self.database[self.collections]
            self.collections.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ =="__main__":
    FILE_PATH="Network_data/phisingData.csv"
    DATABASE="networkdatabase"
    collection='networkdata'
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)

## check data in atlas mongodb
