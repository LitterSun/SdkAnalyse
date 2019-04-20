#
import requests
import os
import json
from apkData import ApkData
from urllib.parse import urlparse, parse_qs

preJson = ""
curJson = ""
apk_data_list = []


def get_apk_json_data():
    url = """http://startpage.wandoujia.com/five/v3/tabs/tops?start=500&max=1300&sessionId=7598048721385334827&pos=m%2Ftops&
v=5.18.1&deviceId=MzU2MTU2MDcxMjkzNjc0&sdk=23&id=wandoujia_android&launchedCount=1&udid=1826abc123374e7eb71ccba877e1e70b6a5cacf2&
channel=tencent_app&rippleSupported=false&vc=12033&capacity=3&launchedAge=0"""
    path = 'json'

    if not os.path.exists(path):
        os.makedirs(path)

    i = 0

    while True:
        if i > 100:
            break
        if i != 0:
            url = preJson["next_url"]
        try:
            r = requests.get(url)
            curJson = r.json()
            f = open(path + '/json_' + str(i) + '.json', 'w')
            f.write(r.content)

            print(url)
            print(r.content)
            f.close()
        except Exception as e:
            raise e
        preJson = curJson
        i += 1


def get_apk_data(data):
    try:
        for apk_data in data["entity"]:
            if is_game_apk(apk_data):
                continue
            useful_apk_data = ApkData()
            useful_apk_data.name = apk_data["title"]
            useful_apk_data.download_url = apk_data['detail']['app_detail']['apk'][0]['download_url']['url']
            useful_apk_data.package_name = parse_qs(urlparse(useful_apk_data.download_url).query)["pn"][0]
            is_cure = False
            for apk in apk_data_list:
                if apk.download_url == useful_apk_data.download_url or apk.package_name == useful_apk_data.package_name:
                    is_cure = True
                    break
            if not is_cure:
                apk_data_list.append(useful_apk_data)

    except Exception as e:
        pass


def is_game_apk(apk_data):
    return apk_data['detail']['app_detail']["app_type"] == 'GAME'


apk_json_dir = os.curdir + os.path.sep + 'apk_json'
for f in os.listdir(apk_json_dir):
    f = open(apk_json_dir + os.path.sep + f, 'r')
    get_apk_data(json.load(f))
    f.close()


class MyEncode(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


f = open('apk_data_list.json', 'w')
json.dump(apk_data_list, f, cls=MyEncode, ensure_ascii=False)
