# 导包 json
import json


# 打开json文件获取文件流
# 使用参数替换 静态文件名
class ReadArticle(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_article(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    data = ReadArticle("article_add.json").read_article()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    print(arrs)
