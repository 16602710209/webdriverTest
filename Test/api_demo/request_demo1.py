import requests
from urllib.parse import urljoin
from urllib.parse import urlencode

# url = 'http://www.renren.com'
# # 1.get请求的简单实现
# def get_test():
#     res = requests.get(url)
#     return res.text
#
# a = get_test()
# print(a)
#
# # 2.post请求的简单实现
# data = {
#
# }
# def post_test():
#     res = requests.post(url='http://xy-log.tagtic.cn', data='/mininfo/v1/logs/webtgbusweb')
#     print(res.json())


# 3.拼接查询字符串
qstr = {
    'sid': '3dGI9zgImvZJ82cH'
}

data = {
    'sid': '3dGI9zgImvZJ82cH',
'stat': 'network_performance',
'connect': '10',
'request': '370',
'receive': '0'
}

url = 'https://rl.mail.qq.com'
path = '/cgi-bin/getinvestigate'


def post_test():
    url_q = urljoin(url, path)
    url_s = urlencode(qstr)
    url_all = url_q + '?' + url_s
    res = requests.post(url=url_all, data=data)
    return res.content()


a = post_test()
print(a)

# 4.headers传参
headers = {

}

def post_test():
    url_q = urljoin(url, path)
    url_s = urlencode(qstr)
    url_all = url_q + '?' + url_s
    res = requests.post(url=url_all, data=data, headers=headers)
    return res.content()

