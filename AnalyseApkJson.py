import json
import os

from ApkData import ApkData


class MyEncode(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def getApkData(data):
    try:
        apks = []
        for apk_data in data["data"]["content"]:
            apkData = ApkData(apk_data["name"], apk_data["downloadUrl"])
            apks.append(apkData)
        return apks

    except Exception as e:
        pass


def analyseJson(path):
    if os.path.isdir(path):
        if os.path.exists(path + os.path.sep + 'apk_data_list.json'):
            os.remove(path + os.path.sep + 'apk_data_list.json')
        apkList = []
        for f in os.listdir(path):
            jsonStr = open(path + os.path.sep + f, 'r')
            apkList = apkList + getApkData(json.load(jsonStr))
            jsonStr.close()
        f = open(path + os.path.sep + 'apk_data_list.json', 'w')
        json.dump(apkList, f, cls=MyEncode, ensure_ascii=False)
        f.close()


analyseJson("/Users/xiangyang/Sparetime/SdkAnalyse/apk_json/影音播放")
