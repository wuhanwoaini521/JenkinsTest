'''
Author: han wu 
Date: 2021-07-13 15:33:44
LastEditTime: 2021-07-13 15:58:26
LastEditors: your name
Description: 
FilePath: /jenkinsTest/page/baidu_page.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''

from base.base import Base

class BaiduPage(Base):
	
	def __init__(self,driver) -> None:
		super().__init__(driver)

	def search_page(self,url):
		self.open(url)