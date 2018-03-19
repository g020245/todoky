from source.YamlStream import getYamlStream
from nested_lookup import nested_lookup as nested
from source.custom_logger import logme

class ConfigGetter:
    # todo refactor
    # todo check if category or setting exists

    def __init__(self, dataStream: dict):
        logme(f"Inicializing ConfigGetter... {self.__str__()} ")
        self.yamlData = dataStream

    def getYamlStream(self):
        return self.yamlData

    def getValue(self, findWhat):
        # todo test
        # todo ref
        """
        Returns a value or collection from config file
        :param findWhat:
        :return:
        """
        logme(f"Trying to get config value for parameter: {findWhat} at {self.__repr__()}")
        return nested(findWhat, self.getYamlStream())



cfg = ConfigGetter(getYamlStream())






