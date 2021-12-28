import logging


info_logger = logging.getLogger(__name__)
warning_logger = logging.getLogger('warning')
info_logger.setLevel(logging.INFO)
# create handlers and set level
stream_handler = logging.StreamHandler()
stream_handler.setLevel(level=logging.INFO)
file_handler = logging.FileHandler('maktab_project.log')
file_handler.setLevel(level=logging.WARNING)
# create formatters and add it to handlers
stream_format = logging.Formatter('%(asctime)s ::%(levelname)s - %(name)s - %(filename)s - %(message)s')
file_format = logging.Formatter('%(asctime)s ::%(levelname)s - %(filename)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)
# add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.debug('this is a debug message')
logger.info('this is an info message')
logger.warning('this is an warning message')
logger.error('this is an error message')
logger.critical('this is an critical message')