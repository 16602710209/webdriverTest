#导包
import unittest
from InterfaceTest.api.api_channels import ApiChannels
from parameterized import parameterized
from InterfaceTest.tools.read_channel_json import ReadChannel

def get_data():
    data = ReadChannel("channel.json").read_channel_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")))
    print(arrs)

# 新建测试类
class TestClannels(unittest.TestCase):
    # 新建测试方法
    @parameterized(get_data())
    def test_channels(self, url, headers, expect_result, status_code):
        # 临时数据
        # url = "http://ttapi.research.itcast.cn/app/v1_0/user/channels"
        # headers = {"Content-type": "application/json",
        #            "Authorization": "Bearer ASJkldhlaskdsfjodfnb"}
        # 调用获取用户频道列表方法
        r = ApiChannels().api_get_channels(url, headers)
        # 调试信息  打印响应结果
        print(r.json())
        # 断言 状态码
        self.assertEquals(status_code, r.status_code)
        # 断言 响应信息
        self.aseertEquals(expect_result, r.json(['message']))

if __name__ == '__main__':
    unittest.main()

