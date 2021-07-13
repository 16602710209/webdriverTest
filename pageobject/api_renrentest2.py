import json

from common.apibase import ApiBase
from pageobject.api_renrentest import Login

api = ApiBase()

class Renren_set():
    def set_ziliao(self):
        url = "http://rrwapi.renren.com/buddy/v1/getFullFriendInfo"

        data = {
            "page": 1,
           "pageSize": 20,
           "userId": "2147542907",
           "appKey": "bcceb522717c2c49f895b561fa913d10",
           "sessionKey": "a1bgS7khctz5FUnx",
           "callId": "1624352386703",
           "sig": "a05e42e587e994f2866f5a034fd38ae5"}
        headers = {
            'Content-Type': 'text/plain'
        }
        res = api.post(url, data, headers=headers)
        if res.status_code == 200:
            return True
        else:
            return False