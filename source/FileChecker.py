from source.config import cfg
from pathlib import Path
from source.custom_logger import logme

class FileChecker(object):

    def __init__(self):
        pass

    def getProgramDirectory(self)->str:
        # todo test
        # todo ref
        """
        Get path as as string to main project directory
        :return:
        """
        return str(cfg.getValue('programDirectory')[0])





    