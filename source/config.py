from source.YamlStream import getYamlStream
from nested_lookup import nested_lookup as nested

class ConfigGetter:
    # todo refactor
    # todo check if category or setting exists

    def __init__(self, dataStream: dict):
        self.yamlData = dataStream

    def getYamlStream(self):
        return self.yamlData

    def getValue(self, findWhat):
        # todo test
        # todo ref
        # todo doc
        return nested(findWhat, self.getYamlStream())



cfg = ConfigGetter(getYamlStream())






