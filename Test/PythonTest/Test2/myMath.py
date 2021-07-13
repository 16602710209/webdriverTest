# 创建一个类
class mymath():
    def jia(self, a, b):
        if isinstance(a, str) and isinstance(b, int):
            b = str(b)
            return a+b
        elif isinstance(a, int) and isinstance(b, str):
            a = str(a)
            return a+b
        else:
            return a+b

    def jian(self, a, b):
        return a-b
    def chengfa(self, a, b):
        return a*b
    def chufa(self, a, b):
        if b==0:
            return "error"
        else:
            return a/b

# 代码功能验证
# if __name__ == "__main__":
#     mm = mymath()
#     # 实现第一条用例
#     actualValue = mm.jia(2, 3)
#     expectValue = 5
#     if actualValue == expectValue:
#         print("该加法功能实现正确")
#
#     # 再来一条用例,本来就是一条异常用例，就应该抛出异常
#     try:
#         actualValue = mm.jia("a", 3)
#     except Exception as e:
#         print("该方法实现正确", e)
#
# # 需求：我们设计的这个方法除了数字的运算外，还能进行字符串的拼接
# # 第三条，验证字符串的加法运算
# try:
#     actualValue = mm.jia("a", "b")
#     expectValue = "ab"
#     if actualValue == expectValue:
#         print("该加法功能实现正确")
# except Exception as e:
#     print(e)