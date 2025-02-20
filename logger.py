import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("search_engine")

def log_request(endpoint: str, params: dict):
    logger.info(f"Запрос к {endpoint}: {params}")

def log_error(error_message: str):
    logger.error(f"Ошибка: {error_message}")
