from loguru import logger


logger.add('logs/file_{time}.log', rotation='4 week', enqueue=True)
