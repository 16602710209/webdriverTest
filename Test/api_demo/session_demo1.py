import requests
from urllib.parse import urljoin, urlencode

# 创建一个会话保持器
s = requests.session()

url = 'https://www.zhihu.com'
path = '/signin'
qstr = {
    'next': '%2F'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
cookies = {
    'SESSIONID': 'Ee8YfG2okIb1T3I6l9mASDkCIzAAFDQZliFLXoNrbqT',
    '_xsrf': 'LzKGMBAMqhBePvqiPh4R5OTq1IYQ4g7Q',
    '_9755xjdesxxd_': '32'
}



def get_test():
    url_q = urljoin(url, path)
    url_s = urlencode(qstr)
    url_all = url_q + '?' + url_s
    res = s.get(url=url_all, headers=headers, cookies=cookies)
    return res.text


a = get_test()
print(a)

