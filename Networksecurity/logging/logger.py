import logging
import os
from datetime import datetime

# Create a log file name using the current date and time in MM_DD_YYYY_HH_MM_SS format
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the full path where the log file will be stored.
# It creates a path like: current_working_directory/logs/LOG_FILE
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the directories in the log path if they do not exist.
# If the folder already exists, it won't raise an error due to exist_ok=True
os.makedirs(logs_path, exist_ok=True)

# Define the complete path of the log file.
# This is the full file path including directory and file name.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module to log messages to the specified file.
# - filename: the log file to write to
# - format: the structure of each log message
# - level: minimum severity of messages to log (INFO and above)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
