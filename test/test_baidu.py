'''
Author: han wu 
Date: 2021-07-13 15:35:26
LastEditTime: 2021-07-13 15:59:56
LastEditors: your name
Description: 
FilePath: /jenkinsTest/test/test_baidu.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''

from page.baidu_page import BaiduPage
from selenium import webdriver as wb
import unittest
from time import sleep

class Test_Case(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = wb.Chrome()
    def test(self):
         page  = BaiduPage(self.driver)
         page.search_page("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
        unittest.main(verbosity=2)


