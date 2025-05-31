import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

# Configuration class to store file paths
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

# Main data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion process")
        try:
            # Read the input dataset
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Dataset loaded into a pandas DataFrame")

            # Create artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved to artifacts/raw.csv")

            # Split the data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Train and test data saved to artifacts/")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )

        except Exception as e:
            logging.error("Error occurred during data ingestion")
            raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        # Data ingestion
        ingestion = DataIngestion()
        train_data_path, test_data_path, _ = ingestion.initiate_data_ingestion()
        
        # Data transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
        # Model training
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        logging.info(f"Model training completed with R2 score: {r2_score:.4f}")
        print(f"Model training completed with R2 score: {r2_score:.4f}")

    except Exception as e:
        logging.error(f"Error in main execution: {e}")
        print(f"Error occurred: {e}")