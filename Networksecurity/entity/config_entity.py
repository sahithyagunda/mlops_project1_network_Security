from datetime import datetime
import os
from networksecurity.constants import training_pipeline

# Print pipeline name (mainly for debugging or logging purposes)
print(training_pipeline.PIPELINE_NAME)


class TrainingPipelineConfig:
    """
    Configuration class for setting up the overall training pipeline.
    This includes creating a unique artifact directory using a timestamp
    to manage and store outputs of different pipeline runs.
    """
    def __init__(self, timestamp=datetime.now()):
        # Format the timestamp to create unique artifact directories
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        # Set pipeline name from constants
        self.pipeline_name = training_pipeline.PIPELINE_NAME

        # Set base artifact directory name
        self.artifact_name = training_pipeline.ARTIFACT_DIR

        # Create a unique artifact directory path using timestamp
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)

        # Store the timestamp
        self.timestamp: str = timestamp


class DataIngestionConfig:
    """
    Configuration class for the data ingestion component of the pipeline.
    This includes paths for feature storage, train/test data, and DB collection info.
    """
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        # Base directory for data ingestion artifacts
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

        # Path where the raw feature data (original CSV) will be stored
        self.feature_store_file: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline.FILE_NAME
        )

        # Path to save the training data after the train/test split
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTTED_DIR,
            training_pipeline.TRAIN_FILE_NAME
        )

        # Path to save the testing data after the train/test split
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTTED_DIR,
            training_pipeline.TEST_FILE_NAME
        )

        # Train-test split ratio for dataset
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO

        # MongoDB collection and database details (if using MongoDB)
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME



class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str =  os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)


class DataTransformationConfig:
     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join( training_pipeline_config.artifact_dir,training_pipeline.DATA_TRANSFORMATION_DIR_NAME )
        self.transformed_train_file_path: str = os.path.join( self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy"),)
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,  training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TEST_FILE_NAME.replace("csv", "npy"), )
        self.transformed_object_file_path: str = os.path.join( self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCESSING_OBJECT_FILE_NAME)
