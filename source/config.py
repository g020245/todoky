from source.YamlStream import getYamlStream


class ConfigGetter:
    # todo refactor
    # todo check if category or setting exists
    def __init__(self, dataStream: dict):
        self.yamlData = dataStream

    def parseSetting(self, inputWords):
        pass





cfg = ConfigGetter(getYamlStream())






