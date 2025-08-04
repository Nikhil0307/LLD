from src.logger import Logger
from conf.Constants import Constants

# Global extra fields if needed (can include machine name, service name, etc.)
default_fields = {"component": "UserService", "hostname": "server01"}

logger = Logger(
    log_dir='logs',
    current_log_level=Constants.INFO,
    console_logging=True,           # Enable console output
    structured_logging=True,        # Log as JSON
    retention_days=7,               # Delete logs older than 7 days
    extra_fields=default_fields     # Global extra fields
)
logger.log("User login successful", level=Constants.INFO, extra_fields={"request_id": "abcd-1234"})
logger.shutdown()

