import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
logs_path = os.path.join(os.getcwd() ,"logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# Define the log file path
LOG_FILE_PATH = os.path.join(logs_path, "application_logs.txt")

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
