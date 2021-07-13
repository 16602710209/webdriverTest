from common.apibase import ApiBase
# import requests
import json

api = ApiBase()
class Login():
    def renren_login(self, user, password):
        url = "http://rrwapi.renren.com/account/v1/loginByPassword"
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Content-Type': 'application/json;charset=utf-8'

        }

        # data = {"user": "13720187233",
        #         "password":"e914aa7b5a650909500c2425d131681b",
        #         "appKey":"bcceb522717c2c49f895b561fa913d10",
        #         "sessionKey":"",
        #         "callId":"1624287787537",
        #         "sig": "c5753e3a4c97736a9fbf07ce947b8e0f"}
        data = json.dumps({
            "user": user,
            "password": password,
            "appKey": "bcceb522717c2c49f895b561fa913d10",
            "sessionKey": "",
            "callId": "1624287787537",
            "sig": "c5753e3a4c97736a9fbf07ce947b8e0f"
        })
        res = api.post(url, data, headers=header)
        return res.json()


        # url = "http://rrwapi.renren.com/account/v1/loginByPassword"
        #
        # payload = json.dumps({
        #     "user": "13720187233",
        #     "password": "e914aa7b5a650909500c2425d131681b",
        #     "appKey": "bcceb522717c2c49f895b561fa913d10",
        #     "sessionKey": "",
        #     "callId": "1624287787537",
        #     "sig": "c5753e3a4c97736a9fbf07ce947b8e0f"
        # })
        # headers = {
        #     'Content-Type': 'application/json'
        # }
        #
        # response = requests.request("POST", url, headers=headers, data=payload)
        #
        # print(response.text)
        # return response.json()
