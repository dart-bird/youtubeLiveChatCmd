import json
import os


def initJsonData(path, initType):
    if not os.path.isfile(path):
        with open(path, 'w') as outfile:
            json.dump(initType, outfile, ensure_ascii=False)
    with open(file=path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def writeJsonData(path, jsonData):
    if not os.path.isfile(path):
        with open(path, 'w', encoding="utf-8") as outfile:
            json.dump(jsonData, outfile, ensure_ascii=False)
    with open(path, 'w', encoding="utf-8") as outfile:
        json.dump(jsonData, outfile, ensure_ascii=False)


def insertJsonData(path, jsonData):
    with open(file=path, encoding="utf-8") as outfile:
        data = json.load(outfile)
    data.update(jsonData)
    with open(file=path, mode='w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False)
    return data


def getJsonData(path):
    with open(file=path, encoding="utf-8") as f:
        data = json.load(f)
    return data
