import logging

logging.basicConfig(filename='myFirstLogger.log', level=logging.INFO)

def logme(message='Nothing to say'):
    logging.info(message)

