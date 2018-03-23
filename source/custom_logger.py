import logging

def testLog(msg):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(f'%(asctime)s:%(levelname)s:%(funcName)s():%({msg})s')
    file_handler = logging.FileHandler('testlog.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)





