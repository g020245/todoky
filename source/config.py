from source.YamlStream import getYamlStream
from nested_lookup import nested_lookup as nested
# from source.custom_logger import logme

class ConfigGetter:
    # todo refactor
    # todo check if category or setting exists

    def __init__(self, dataStream: dict):
        self.yamlData = dataStream

    def getYamlStream(self):
        return self.yamlData

    def getValue(self, findWhat:str, subSetting:str='')->list:
        # todo test
        # todo ref
        # todo doc
        """
        Get value from config file.
        Find what returns a list with one item o subcategories in searched config entry.
         If subsetting is provided then it returns that subsetting.
        :param findWhat:
        :return:
        """
        resultFromYaml: list = nested(findWhat, self.getYamlStream())

        if subSetting:
            return nested(subSetting, resultFromYaml)
        else:
            return resultFromYaml


config = ConfigGetter(getYamlStream())





