from common.apibase import ApiBase

api = ApiBase()


class Login():


    def login(self):
        """163邮箱登录"""
        url = 'https://countly.mail.163.com/stats/i'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "app_key": "free_webmail_9c89159b6fde1dc2",
            "common": "{'ua':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0','browser':'Firefox','browser_version':'89.0','os':'Windows','os_version':'10','device':'desktop','resolution':'1920x1080','referrer':'','site_channel':'default','client':'pc','density':'@1x','locale':'zh-CN','manufacturer':'','domain':'mail.163.com','app_version':'6.0b2106162038','abtest_zone':'','abtest_version':'','carrier':'','app_channel':'','ip':'','lbs':'','network_type':'','uid':'13720187233@163.com','dashi_uid':'','account':'m13720187233_1@163.com'}",
            "device_id": "4f58b600a8c4b4300355163a5132e61a",
            "dow": "1",
            "events": "[{'key':'webmail_index_view','count':1,'segmentation':{},'path_trace':[],'session_id':'235F55C3-3EC8-4B45-A5B5-909A9F6066D3','type':'pv','module_name':'webmail_index_view','utm':{'utm_id':'','utm_source':'','utm_medium':'','utm_term':'','utm_content':'','utm_campaign':''},'domInfo':{},'timestamp':1624269873802,'hour':18,'dow':1,'tz':480},{'key':'deftabclick','count':1,'segmentation':{'value':'t0','sid':'bDkeTioOeFHryVPNMWOOJoMnNxvtXELe'},'path_trace':[],'session_id':'235F55C3-3EC8-4B45-A5B5-909A9F6066D3','type':'click','module_name':'webmail_index_view','utm':{'utm_id':'','utm_source':'','utm_medium':'','utm_term':'','utm_content':'','utm_campaign':''},'domInfo':{'type':'click','x':0,'y':0,'width':1231,'height':765,'targetName':'','className':'','id':'','dataset':{}},'timestamp':1624269874260,'hour':18,'dow':1,'tz':480}]",
            "hour": "18",
            "timestamp": "1624269874826",
            "tz": "480",
            "version": "1.0"
        }

        res = api.get(url, data, headers=header)
        return res.json()



if __name__ == '__main__':
    lg = Login()
    a = lg.login()
    print(a)
