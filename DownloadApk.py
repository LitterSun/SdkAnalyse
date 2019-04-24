import threading

import requests
import json
import os
import queue

from ApkData import ApkData


def as_payload(dct):
    return ApkData(dct['name'], dct['downloadUrl'], dct['categoryName'])


q = queue.Queue()
apk_json = os.curdir + os.path.sep + "apk_json"
for f in os.listdir(apk_json):
    f = open(apk_json + os.path.sep + f + os.path.sep + 'apk_data_list.json', 'r')
    apk_list = json.load(f, object_hook=as_payload)
    for item in apk_list:
        q.put(item)


def download_apk():
    while True:
        download_apk_data = q.get()
        re_count = 0
        if not os.path.exists('../apk'):
            os.mkdir('../apk')
        if not os.path.exists('../apk/' + download_apk_data.categoryName):
            os.mkdir('../apk/' + download_apk_data.categoryName)
        apk_filename = '../apk/' + download_apk_data.categoryName + os.path.sep + download_apk_data.name + '.apk'
        if os.path.isfile(apk_filename):
            print("has download:" + apk_filename)
        else:
            while True:
                try:
                    print("start download:" + apk_filename)
                    re = requests.get(download_apk_data.downloadUrl)
                    if re.status_code == 200:
                        with open(apk_filename, 'wb') as fd:
                            for c in re.iter_content(1000):
                                fd.write(c)
                            print(fd.name)
                except Exception as e:
                    print(e)
                    re_count += 1
                    if re_count > 4:
                        print("download fail:" + apk_filename)
                    continue
                else:
                    print("download success:" + apk_filename)
                    break
        q.task_done()


for i in range(5):
    t = threading.Thread(target=download_apk)
    t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
    t.start()

q.join()
