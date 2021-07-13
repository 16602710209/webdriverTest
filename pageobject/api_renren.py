import requests #导入安装的模块。这个模块专门处理请求

class RRapi(): #新建一个人人网的接口类，这个类下专门写人人网的接口

    def login(self): #定义一个函数名，不给他传参数，self默认值为固定写法，只要是写在class底下的函数都有self
        '''用户登录'''
        url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021141353548'  #请求地址，从fiddler复制来的
        body = {                                                                         #请求体body，从fiddler复制来的
            "email":"17865517994",
            "icode":"",
            "origURL":"http://www.renren.com/home",
            "domain":"renren.com",
            "key_id":"1",
            "captcha_type":"web_login",
            "password":"6b0f07a2a04f2975752196b1be667cd6a8c426b7be0f030a5f576dc605541cf8",
            "rkey":"9635eab3a4b2a5952b56441f0ac2a547",
            "f":""
        }
        s = requests.session()  #这是固定写法，代表事先建立一个会话保持 s,登录请求成功后，s会自动的保持与接口后台的连通
        res = s.post(url=url,data=body)  #用这个会话s来发post请求，给post()方法传入地址和请求体两个参数
        print(res.text)
        assert res.json()['code'] == True  #断言响应结果中的code参数的值是否为True；res.json()['code']这是在{}字典中取code的值
        return s


    def edit_hobby(self,music,interest,book,movie,game,comic,sport='足球'):
        '''编辑爱好'''
        url = 'http://www.renren.com/PersonalInfo.do?v=info_timeline' #请求地址，从fiddler复制来的
        body = {                                                      #请求体body，从fiddler复制来的
            "music":music,
            "interest":interest,
            "book":book,
            "movie":movie,
            "game":game,
            "comic":comic,
            "sport":sport,
            "errorReturn":"1",
            "submit":"保存",
            "requestToken":"-2038961981",
            "_rtk": "5238e71d"
        }
        s = self.login()  #先调用登录方法，先执行登录，得到登陆后的会话s
        res = s.post(url=url,data=body) #用登录后的会话发送post请求，返回请求响应给res变量
        print(res.text)
        if res.status_code == 200:  #res是响应，res.status_code表示获取响应的状态码；判断响应的状态码是否为200.
            return True  #如果是200则返回True
        else:
            return False #如果不是200则返回False

if __name__ == "__main__":
    api = RRapi()
    api.login()
