import logging

# Configure the logging system
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a logger instance
logger = logging.getLogger()

def log_info(message: str):
    """Log an info message."""
    logger.info(message)

def log_error(message: str):
    """Log an error message."""
    logger.error(message)

def log_success(message: str):
    """Log a success message."""
    logger.info(f"SUCCESS: {message}")

def log_warning(message: str):
    """Log a warning message."""
    logger.warning(message)

def log_debug(message: str):
    """Log a debug message."""
    logger.debug(message)
