#!usr/env/bin python3
# -*- coding: utf-8 -*-

# @Time    : 2019/7/23 20:36
# @Author  : wq
# @Site    : 
# @File    : testFengzhuang.py

import sys
sys.path.append('..')

from Public.test_requests import requ


reques=requ()
class TestApi(object):
    def __init__(self,url,key,connent,fangshi):
        self.url=url
        self.key=key
        self.connent=connent
        self.fangshi=fangshi
        
    def testapi(self):
        if self.fangshi=='POST':
            self.response=reques.post(self.url,self.connent)
            
        elif self.fangshi=="GET":
            self.response = reques.get(url=self.url,params=self.connent)
            
        return self.response
    
    def getJson(self):
        json_data = self.testapi()
        return json_data