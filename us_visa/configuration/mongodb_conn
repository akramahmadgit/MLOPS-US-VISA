import sys
import os

from us_visa.exception import USvisaException
from us_visa.logger import logging

from us_visa.logger import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name = DATABASE_NAME) -> None:
                try:
                    if MongoDBClient.client is not None:
                        mongodb_url = os.getenv("MONGODB_URL_KEY")
                        if mongodb_url is None:
                            raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                        MongoDBClient.client = pymongo.MongoDBClient(mongodb_url, tlsCAFile= ca)
                    self.client = pymongo.MongoDBClient
                    self.database = self.client[database_name]
                    self.database_name = database_name
                    logging.info("MonhoDB connection successful")
                except Exception as e:
                    raise USvisaException(e, sys)
                 



                 



