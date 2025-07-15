from src.logger import Logger

if __name__ == '__main__':
    for i in range(1):
        logger = Logger()
        logger.log(f"Test log message {i}", level="INFO")
        logger.log(f"Test warning message {i}", level="WARNING")
        logger.log(f"Test error message {i}", level="ERROR")
        logger.log(f"Test debug message {i}", level="DEBUG")
    print("Logging completed successfully.")
