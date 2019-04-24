import queue
import subprocess
import os
import threading

print("start unzip:")
q = queue.Queue()
apk_json_dir = '../apk/金融理财'
for f in os.listdir(apk_json_dir):
    f = f.replace('.apk', '')
    path = os.path.abspath(apk_json_dir + '/' + f)
    if not os.path.exists(path):
        q.put(path)


def apk_to_class():
    while True:
        apk_path = q.get()
        apk_file = apk_path + ".apk"
        re_count = 0
        while True:
            try:
                print("start unzip:" + apk_file)
                os.system("apktool d " + apk_file.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)") + " -o " + apk_path.replace(" ", "\\ ").replace("(", "").replace(")", ""))
            except Exception as e:
                print(e)
                re_count += 1
                if re_count > 4:
                    print("unzip fail:" + apk_path)
                continue
            else:
                print("unzip success:" + apk_path)
                break
        q.task_done()


for i in range(5):
    a = 'test'
    t = threading.Thread(target=apk_to_class)
    # thread dies when main thread (only non-daemon thread) exits.
    t.daemon = True
    t.start()

q.join()
