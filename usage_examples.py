from kyoo_log.logger import KyooLogger

logger = KyooLogger(__name__)

logger.info("This is an info message.")
logger.warning("This is a warning message.")
try:
    x = 1 / 0
except ZeroDivisionError as e:
    logger.error(f"An error occurred: {e}")
    logger.critical("Application stopped due to a fatal error.", exc_info=True)