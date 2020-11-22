# -*- coding: utf8 -*-
import requests
import hashlib
import json
import time
import random
requests.packages.urllib3.disable_warnings
def md5(code):
    res=hashlib.md5()
    res.update(code.encode("utf8"))
    return res.hexdigest()

def get_information(mobile,password):
    header = {
        'Content-Type': 'application/json; charset=utf-8',
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-G9500 Build/PPR1.180610.011)"
    }
    url="https://sports.lifesense.com/sessions_service/login?version=4.5&systemType=2"
    datas = {
        "appType":6,
        "clientId":'8e844e28db7245eb81823132464835eb',
        "loginName":str(mobile),
        "password":md5(str(password)),
        "roleType":0
        }
    response =requests.post(url,headers=header,data=json.dumps(datas))
    return response.text

def update_step(step,information):
    step =int(step)
    url="https://sports.lifesense.com/sport_service/sport/sport/uploadMobileStepV2?version=4.5&systemType=2"
    accessToken=json.loads(information)["data"]["accessToken"]
    userId=json.loads(information)["data"]["userId"]
    #print(json.loads(information))
    #print(accessToken)
    #print(userId)
    #获取当前时间和日期
    timeStamp=time.time()
    localTime = time.localtime(timeStamp)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
    print(strTime)
    measureTime=strTime+","+str(int(timeStamp))

    header = {
    'Cookie': 'accessToken='+accessToken,
    'Content-Type': 'application/json; charset=utf-8',
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-G9500 Build/PPR1.180610.011)"
    }
    sport_datas = {
        "list": [
            {
                 "DataSource":2,
                #"active":0,
                 "calories":str(int(step/4)),
                #"dataSource":4,
                 "deviceId":"M_NULL",
                 "distance":str(int(step/3)),
                 "exerciseTime":0,
                 "isUpload":0,
                 "measurementTime":measureTime,
                #"priority":0,
                 "step": str(step),
                 "type":2,
                 "updated":str(int(time.time()*1000)),
                 "userId":str(userId)
                }]
                }
    result=requests.post(url,headers=header,data=json.dumps(sport_datas))
    # print(result.text)
    return result.text

def bind(information):
    # 设备qrcode列表
    qrcodelist = ['http://we.qq.com/d/AQC7PnaOelOaCg9Ux8c9Ew95yumTVfMcFuGCHMY-', 'http://we.qq.com/d/AQC7PnaOysMBFUhD6sByjYwH2MT12Jf2rqr2kFKm', 'http://we.qq.com/d/AQC7PnaOEcpmVUpHtrZBmRUVq4wOOgKw-gfh6wPj', 'http://we.qq.com/d/AQC7PnaOuG5SHierDiEH2AdZLzMt3W__GL8E1MJj', 'http://we.qq.com/d/AQC7PnaOC0S07XFU-c_R1cpxY1mtf8oiXiDrXET7', 'http://we.qq.com/d/AQC7PnaOoraxuZEdkFyVSO6gaTvMjzEzhEfLRXbE', 'http://we.qq.com/d/AQC7PnaOhQxO8K2EuU44QBZ8cRzB2ofP-oFJSU_6', 'http://we.qq.com/d/AQC7PnaOmwgxedHWCLVr-ZyeoLxHtRrHBGDuyH9E', 'ttp://we.qq.com/d/AQC7PnaO4am4196RIo98NYn_vPfHN-Y5j-w9FmSN', 'http://we.qq.com/d/AQC7PnaO2WczbXNLV7PzC7V60i7-iOgLha5Bg4cV', 'http://we.qq.com/d/AQC7PnaOZAUJTMxJ6-gbdrWV6y-jHHofCYFl-Jv0']

    accessToken = json.loads(information)["data"]["accessToken"]
    userId = json.loads(information)["data"]["userId"]
    header = {
        'Cookie': 'accessToken=' + accessToken,
        'Content-Type': 'application/json; charset=utf-8',
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-G9500 Build/PPR1.180610.011)"
    }
    for i in qrcodelist:
        datas = {
            "qrcode": i,  
            "userId": userId,
        }
        url = 'https://sports.lifesense.com/device_service/device_user/bind'
        result = requests.post(url,headers=header,data=json.dumps(datas))
        if result.status_code == '401':
            print('重新登录')
            main()
        else:
            msg = result.json()
            print(msg)
            if msg.get('msg') == '成功':
                print('绑定成功，即将开刷')
                break
            else:
                print('此设备绑定失败,尝试下一个。')
    print('所有设备均无法绑定，请自己寻找可用的qrcode，将连接加入列表qr中进行尝试。')
    
def server_send(msg):
    if sckey == '':
        return
    server_url = "https://sc.ftqq.com/" + str(sckey) + ".send"
    data = {
            'text': msg,
            'desp': msg
        }
    requests.post(server_url, data=data)

def kt_send(msg):
    if ktkey == '':
        return
    kt_url = 'https://push.xuthus.cc/send/'+str(ktkey)
    data = ('步数刷取完成，请查看详细信息~\n'+str(msg)).encode("utf-8")
    requests.post(kt_url, data=data)

def execute_walk(phone,password,step):
    information=get_information(phone,password)
    bind(information)
    update_result=update_step(step,information)
    result=json.loads(update_result)["msg"]
    if result == '成功':
        msg = "刷新步数成功！此次刷取" + str(step) + "步。"
        print(msg)
        server_send(msg)
        kt_send(msg)
    else:
        msg = "刷新步数失败！请查看云函数日志。"
        print(msg)
        server_send(msg)
        kt_send(msg)


def main():
    if phone and password and step != '':
        execute_walk(phone, password, step)
    else:
        print("参数不全,请指定参数。或者在调用中直接指定参数")

# -- 配置 --
# ------------------------------
phone = ''  # 登陆账号
password = ''  # 密码
step = random.randint(8000,10000)  # 随机8000-10000步数
sckey = ''  # server酱key(可空)
ktkey = ''  # 酷推key(可空)
# ------------------------------

def main_handler(event, context):
    return main()

if __name__ == '__main__':
    main()

