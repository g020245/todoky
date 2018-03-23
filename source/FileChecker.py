from source.config import config
import os
import glob
from pathlib import Path
from source.custom_logger import logMeDEBUG



class FileChecker(object):

    def __init__(self):
        pass

    def getProgramDirectory(self)->str:

        # todo ref
        """
        Get path as as string to main project directory
        :return:
        """
        return str(config.getValue('programDirectory')[0])

    def getMainInputPath(self):
        # todo test
        # todo ref
        """
        Get a valid input directory from config
        :return:
        """

        return str(config.getValue('mainInputPath')[0])

    def getFileAndDirectoryListInPath(self, path:str)->list:
        # todo test
        # todo ref
        """
        Get a list of items in path
        :param path:
        :return:
        """

        return glob.glob(path)

    def getInputFolderItemPaths(self):
        # todo test
        # todo ref
        """
        Get contents if main input directory.
        :return:
        """
        a = 150
        logMeDEBUG(f"This is cool: {a}")
        inputPath = self.getMainInputPath()
        endOfPath = str('\\*')
        return os.listdir(inputPath)



fc = FileChecker()


print(f"{fc.getInputFolderItemPaths()}")


    