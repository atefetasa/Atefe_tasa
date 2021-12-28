import logging


info_logger = logging.getLogger(__name__)
warning_logger = logging.getLogger('warning')
info_logger.setLevel(logging.INFO)
# create handlers and set level
info_handler = logging.FileHandler('info.log')
warning_handler = logging.FileHandler('warning.log')
info_handler.setLevel(level=logging.INFO)
warning_handler.setLevel(level=logging.WARNING)
# create formatters and add it to handlers
file_format = logging.Formatter('%(asctime)s ::%(levelname)s - %(filename)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
info_handler.setFormatter(file_format)
warning_handler.setFormatter(file_format)
# add handlers to the logger
info_logger.addHandler(info_handler)
warning_logger.addHandler(warning_handler)
