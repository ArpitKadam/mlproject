import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info('Data Ingestion Started')
            df = pd.read_csv("./data/stud.csv")
            logging.info("Data Read Successfully")
            logging.info("Data Shape: {}".format(df.shape))
            logging.info("Data Columns: {}".format(df.columns))
            logging.info("Data Head: {}".format(df.head()))
            logging.info("Data Info: {}".format(df.info()))
            logging.info("Data Describe: {}".format(df.describe()))

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('Data Saved in Artifacts folder Successfully')

            logging.info('Train Test Split Started')
            train, test = train_test_split(df, test_size=0.2, random_state=42)
            logging.info('Train Shape: {}'.format(train.shape))
            logging.info('Test Shape: {}'.format(test.shape))
            logging.info('Saving Train and Test Data in Artifacts folder')
            train.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Train and Test Data Saved Successfully')
            logging.info('Train Test Split Completed')

            logging.info('Data Ingestion Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )

        except Exception as e:
            logging.info(f'Error in Data Ingestion: {str(e)}')
            raise CustomException(f'Error in Data Ingestion: {str(e)}')
        
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()