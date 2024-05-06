from dotenv import load_dotenv
import logging
import sys
import os

# Load the environment variables
load_dotenv()

# Initiate the logger
logger = logging.getLogger(__name__)

# Set a formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Setup log file configuration
logging.basicConfig(filename=os.environ['LOG_FILENAME'],
                    encoding=os.environ['LOG_ENCODING'], level=logging.DEBUG)

# Setup log on stdout
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

# Add the stdout handler
logger.addHandler(handler)
