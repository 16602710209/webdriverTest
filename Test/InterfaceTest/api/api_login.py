"""
目标：实现登录接口对象封装
"""

# 导包
import requests


# 新建类 登录接口对象
class ApiLogin(object):
    # 新建方法 登录方法
    def api_post_login(self, url, obile, code):
        # headers 定义
        headers = {"Content-Type": "application/json"}
        # data报文 定义
        data = {"mobile": mobile, "code": code}
        # 调用post并返回相应对象
        return requests.post(url, headers, data)


"""
提示：
    url、mobile、code：最后都需要从data数据文件读取出来，做参数化使用，所以这里我们动态传参
"""
