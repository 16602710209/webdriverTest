# 导包 unittest ApiArticle
import unittest
from InterfaceTest.api.api_articel import ApiArticle
from parameterized import parameterized
from InterfaceTest.tools.read_json_article import ReadArticle
from InterfaceTest.tools.read_json_article_delete import ReadArticleDelete

def get_data():
    data = ReadArticle("article_add.json").read_article()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs

def get_delete_data():
    datas = ReadArticleDelete("article_delete.json").read_article_delete()
    arrs = []
    arrs.append((datas.get("url"),
                 datas.get("headers"),
                 datas.get("data"),
                 datas.get("expect_result"),
                 datas.get("status_code")))
    return arrs
# 新建测试类 继承
class TestArticle(unittest.TestCase):
    # 新建收藏文章方法
    @parameterized.expand(get_data())
    def test01_collection(self, url, headers, data, expect_result, status_code):
        # 临时数据
        # 调用收藏文章
        r = ApiArticle().api_post_collection(url, headers, data)
        print("收藏响应数据为：", r.json())
        # 断言
        self.assertEquals(status_code, r.status_code)
        # 断言响应信息
        self.assertEqual(expect_result, r.json()["message"])
    # 新建取消收藏文章方法
    @parameterized.expand(get_delete_data())
    def test02_cancel(self, url, headers, data, expect_result, status_code):
        # 调用去取消收藏方法
        r = ApiArticle.api_delete_article(url, headers)
        # 断言状态码
        self.assertEquals(status_code, r.status_code)

if __name__ == '__main__':
    unittest.main()
