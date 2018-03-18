import yaml
import time
import datetime
from source.helpers import paths

def getYamlStream():
    # todo test
    # todo ref
    # todo doc
    '''

    :return:
    '''
    with open(paths['configPath'], encoding='utf8') as configFile:
        stream = configFile.read()
    return yaml.load(stream)



# def listContainsOnlyStrings(lst:list)->bool:
#     if len(lst) < 1:
#         return False
#     for i in lst:
#         if type(i) != str:
#             return False
#     return True
#
# def timing(f):
#     def wrap(*args):
#         time1 = time.time()
#         ret = f(*args)
#         time2 = time.time()
#         print(f"{f.__name__} function took {(time2-time1)}  ")
#         #print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
#         return ret
#     return wrap
#
#
# def removeEmptyValuesInList(list: list) -> list:
#     """ Iterate trough list and remove empty values from it"""
#
#     return [i for i in list if i != '']
#
#
# def sanitizeString(inputString, sanitizeFrom=''):
#     '''
#     sanitize a string.
#     :param inputString:
#     :return:
#     '''
#     thingsToRemove = [
#         '\n',
#         '\t',
#     ]
#
#     if sanitizeFrom:
#         thingsToRemove.append(str(sanitizeFrom))
#
#     if type(inputString) != str:
#         return
#
#     stripped = str(inputString).strip()
#     for thing in thingsToRemove:
#         if thing in stripped:
#             stripped = inputString.replace(thing, '')
#             if not stripped:
#                 return
#
#     return stripped
#
#
# def parseDate(dateFromConfig: str) -> str:
#     '''
#     Take a date from input file like d02/02 and convert to sring 2017-02-02
#
#     :param dateFromConfig:
#     :return:
#     '''
#     year = int(2018)
#     month = int(dateFromConfig[1:3])
#     day = int(dateFromConfig[4:6])
#
#     return str(datetime.datetime(year, month, day).date())
#
#
# def splitAndKeepDelimiter(string: str) -> list:
#     return string.splitlines(True)
#
#
# def makeALineDict(date: str, category: str, line: str) -> dict:
#     di = {
#         'date': date,
#         'category': category,
#         'line': line
#     }
#
#     return di

