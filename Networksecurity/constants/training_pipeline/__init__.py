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
