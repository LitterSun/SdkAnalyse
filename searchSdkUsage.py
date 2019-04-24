import os
import csv


def findOkHttp(path):
    if os.path.isdir(path):
        result = os.popen('find ' + path.replace(" ", "\\ ") + ' -name' + " \"*okhttp*\"").readlines()
        if len(result) > 0:
            return True

        result = os.popen('find ' + path.replace(" ", "\\ ") + ' -name' + " publicsuffixes.gz").readlines()
        if len(result) > 0:
            return True
    return False


def findJPush(path):
    if os.path.isdir(path):
        result = os.popen(
            "cat " + path.replace(" ", "\\ ") + "/AndroidManifest.xml| grep cn.jpush.android.service.PushService").readlines()
        if len(result) > 0:
            return True
    return False


def findGetui(path):
    if os.path.isdir(path):
        result = os.popen("cat " + path.replace(" ", "\\ ") + "/AndroidManifest.xml| grep com.igexin.sdk.PushService").readlines()
        if len(result) > 0:
            return True
    return False


def findUmeng(path):
    if os.path.isdir(path):
        result = os.popen("cat " + path.replace(" ", "\\ ") + "/AndroidManifest.xml| grep com.umeng.message.UmengMessage").readlines()
        if len(result) > 0:
            return True
    return False


def findXinge(path):
    if os.path.isdir(path):
        result = os.popen("cat " + path.replace(" ", "\\ ") + "/AndroidManifest.xml| grep com.tencent.android.tpush").readlines()
        if len(result) > 0:
            return True
    return False


def findMiPush(path):
    if os.path.isdir(path):
        result = os.popen("cat " + path.replace(" ", "\\ ") + "/AndroidManifest.xml| grep com.xiaomi.push.service.XMPushService").readlines()
        if len(result) > 0:
            return True
    return False


def findHmsPush(path):
    if os.path.isdir(path):
        result = os.popen("cat " + path.replace(" ", "\\ ") + "/AndroidManifest.xml| grep com.huawei.android.push.intent").readlines()
        if len(result) > 0:
            return True
    return False


def findMeizuPush(path):
    if os.path.isdir(path):
        result = os.popen("cat " + path.replace(" ", "\\ ") + "/AndroidManifest.xml| grep com.meizu.flyme.push.intent").readlines()
        if len(result) > 0:
            return True
    return False


sdkCsv = os.curdir + os.path.sep + 'SdkUsage.csv'
if os.path.exists(sdkCsv):
    os.remove(sdkCsv)
out = open('SdkUsage.csv', 'w', newline='')
csv_write = csv.writer(out, dialect='excel')
csv_write.writerow(
    ['APP', 'OkHttp', '极光推送', '个推推送', '友盟推送', '小米推送', '信鸽推送', '华为推送', '魅族推送'])

apk_dir = '../apk/金融理财'
for f in os.listdir(apk_dir):
    appName = f
    f = os.path.abspath(apk_dir + '/' + f)
    if os.path.isdir(f):
        OkHttp = "NO"
        Jpush = "NO"
        Getui = "NO"
        Umeng = "NO"
        MiPush = "NO"
        Xinge = "NO"
        Huawei = "NO"
        Meizu = "NO"
        if findOkHttp(f):
            OkHttp = "YES"
            print(f + " find OkHttp")
        if findJPush(f):
            Jpush = "YES"
            print(f + " find Jpush")
        if findGetui(f):
            Getui = "YES"
            print(f + " find Getui")
        if findUmeng(f):
            Umeng = "YES"
            print(f + " find Umeng")
        if findMiPush(f):
            MiPush = "YES"
            print(f + " find MiPush")
        if findXinge(f):
            Xinge = "YES"
            print(f + " find Xinge")
        if findHmsPush(f):
            Huawei = "YES"
            print(f + " find Huawei")
        if findMeizuPush(f):
            Meizu = "YES"
            print(f + " find Meizu")
        csv_write.writerow(
            [appName, OkHttp, Jpush, Getui, Umeng, MiPush, Xinge, Huawei, Meizu])
