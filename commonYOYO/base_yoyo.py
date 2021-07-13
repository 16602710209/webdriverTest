from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self, locator):
        '''定位元素方法'''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele

    def findElements(self, locator):
        '''定位一组元素方法'''
        eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
        return eles

    def click(self, locator):
        '''点击的方法'''
        ele = self.findElement(locator)
        ele.click()

    def sendKeys(self, locator, text):
        '''输入位文本的方法'''
        ele = self.findElement(locator)
        ele.send_keys(text)

    def clear(self, locator):
        '''清空方法'''
        ele = self.findElement(locator)
        ele.clear()



if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    baidu = Base(driver)
    locl = (By.ID, "kw")
    baidu.findElement(locl).send_keys("haha")

