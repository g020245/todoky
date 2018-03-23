from source.custom_logger import testLog
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('testlog.log')
formatter = logging.Formatter(f'%(asctime)s:%(levelname)s:%(funcName)s():%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def oneFunc():
    a = 150
    b = 200
    logging.info('This is one Func')
    return 'This is one FUnc'

oneFunc()