import requests
from flask import *
import json
app = Flask(__name__)
@app.route("/vf",methods=["GET"]) 
def check():
    number = "xxxx"
    password = "xxxx"
    url1="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
    hd1={
    'Accept':'application/json, text/plain, */*',
	'Connection':'keep-alive',
	'x-dynatrace':'MT_3_13_3830690492_8-0_a556db1b-4506-43f3-854a-1d2527767923_0_16912_686',
	'x-agent-operatingsystem':'V12.0.17.0.QJQMIXM',
	'clientId':'AnaVodafoneAndroid',
	'x-agent-device':'lime',
	'x-agent-version':'2022.1.2.3',
	'x-agent-build':'500',
	'Content-Type':'application/x-www-form-urlencoded',
	'Content-Length':'145',
	'Host':'mobile.vodafone.com.eg',
	'User-Agent':'okhttp/4.9.1'
    }
    data1={"username":""+number+"","password":""+password+"","grant_type":"password","client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3","client_id":"my-vodafone-app"
    }
    r1=requests.post(url1,headers=hd1,data=data1).json()
    toc=r1['access_token']
    ss="Bearer "+toc
    url=f"https://web.vodafone.com.eg/services/dxl/pim/product?relatedParty.id={number}&place.@referredType=Local&@type=MIProfile"
    headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua-platform': "\"Android\"",
  'Authorization': ss,
  'Accept-Language': "AR",
  'msisdn': number,
  'sec-ch-ua': "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
  'clientId': "WebsiteConsumer",
  'sec-ch-ua-mobile': "?1",
  'Content-Type': "application/json",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://web.vodafone.com.eg/spa/flexManagement/internet",
    }
    resp = requests.get(url,headers=headers).json()
    js=resp[1]["productOffering"]["encProductId"]
#print(js)
    url3 = "https://web.vodafone.com.eg/services/dxl/pom/productOrder"
    payload3 = {
    "channel": {
    "name": "MobileApp"
  },
  "orderItem": [
    {
      "action": "add",
      "product": {
        "characteristic": [
          {
            "name": "ExecutionType",
            "value": "Sync"
          },
          {
            "name": "LangId",
            "value": "en"
          },
          {
            "name": "MigrationType",
            "value": "Repurchase"
          },
          {
            "name": "OneStepMigrationFlag",
            "value": "Y"
          },
          {
            "name": "DropAddons",
            "value": "True"
          }
        ],
        "relatedParty": [
          {
            "id": number,
            "name": "MSISDN",
            "role": "Subscriber"
          }
        ],
        "id": "MI_BASIC_SUPER_20",
        "@type": "MI",
        "encProductId": js
      }
    }
  ],
  "@type": "MIProfile"
    }
    headers3 = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'sec-ch-ua-platform': "\"Android\"",
  'Authorization': ss,
  'Accept-Language': "AR",
  'sec-ch-ua': "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
  'msisdn': number,
  'clientId': "WebsiteConsumer",
  'x-dtpc': "8$469604226_683h42vQQHFJQPHIMDFKPTHALAATUCLCJHPDWDS-0e0",
  'sec-ch-ua-mobile': "?1",
  'Origin': "https://web.vodafone.com.eg",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://web.vodafone.com.eg/spa/flexManagement/internet",
    }
    response3 = requests.post(url3, data=json.dumps(payload3), headers=headers3)
    return response3.json()

if __name__ ==  '__main__' :
	app.run(host= '0.0.0.0' , port=8080)

