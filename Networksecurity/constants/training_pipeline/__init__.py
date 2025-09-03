import os
import sys
import numpy as np
import pandas as pd

"""
Constants used across the Data Ingestion pipeline.
These are used for naming directories, files, and other static configurations.
"""

# MongoDB-related constants for data ingestion
DATA_INGESTION_COLLECTION_NAME: str = "networkdata"
DATA_INGESTION_DATABASE_NAME: str = "networkdatabase"

# Directory names used in data ingestion
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTTED_DIR: str = "ingested"

# Train-test split ratio
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

"""
Constants used for the overall training pipeline.
"""

# Target column in dataset
TARGET_COLUMN = "Result"

# Name of the pipeline and artifact root directory
PIPELINE_NAME: str = "Networksecuritypipeline"
ARTIFACT_DIR: str = "Artifacts"

# Input and output file names
FILE_NAME: str = "phisingData.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")
SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"



## Data validation constants -- starts with DATA_VALIDATION VAR NAME

DATA_VALIDATION_DIR_NAME:str ="data_validation"
DATA_VALIDATION_VALID_DIR:str="validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"

PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessing.pkl"


"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"


"""
Model Trainer ralated constant start with MODE TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05

TRAINING_BUCKET_NAME = "netwworksecurity"
