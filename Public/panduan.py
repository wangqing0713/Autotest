#!usr/env/bin python3
# -*- coding: utf-8 -*-

# @Time    : 2019/7/23 20:36
# @Author  : wq
# @File    : panduan.py

import sys
sys.path.append('..')


from Public.fengzhuang_dict import res
from Public.log import LOG,logger


@logger('断言测试结果')
def assert_in(asserqiwang,fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')   
        result = dict([(item.split('=')) for item in data])        
       
        for key in result.keys():
            value1=res(fanhuijson,key)
        
        value2=([(str(value)) for value in result.values()])        
        
        if value1==value2:
            return {'code':0,"result":'pass'}
        else:
            return {'code':1,'result':'fail'}
        
    elif asserqiwang == fanhuijson['result']:
        return  {'code':0,"result":'pass'}   
    
    else:
        LOG.info('填写测试预期值')
        return  {"code":2,'result':'填写测试预期值'}
    
@logger('断言测试结果')
def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info('填写测试预期值')
        raise {"code":1,'result':'填写测试预期值'}
    
    
if __name__=="__main__":
    asserqiwang='code=0'
    fanhuijson = {'code': 0, 'result': '{"redirect":"https://www.uat.art2print.cn"}'}
    assert_in(asserqiwang, fanhuijson)