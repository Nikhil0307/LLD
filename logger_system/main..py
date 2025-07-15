from src.logger import Logger
from conf.Constants import Constants

if __name__ == "__main__":
    logger = Logger()
    for i in range(10):
        logger.log(f"Test info {i}", level=Constants.INFO)
        logger.log(f"Test warn {i}", level=Constants.WARNING)
        logger.log(f"Test error {i}", level=Constants.ERROR)
    logger.shutdown()
