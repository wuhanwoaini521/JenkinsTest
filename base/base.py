'''
Author: han wu 
Date: 2021-07-13 15:31:51
LastEditTime: 2021-07-13 15:33:30
LastEditors: your name
Description: 
FilePath: /jenkinsTest/base/base.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''


class Base:
        
        def __init__(self,driver) -> None:
                self.driver = driver
	
	def open(self,url = None):
         if url:
         	self.driver.get(url)
         else:
                 self.driver.get(self.url)