#!usr/env/bin python3
# -*- coding: utf-8 -*-

# @Time    : 2019/7/23 20:36
# @Author  : wq
# @File    : run_http_html.py

import sys
sys.path.append('..')

import os,datetime,time
from testCase.case import testinterface
from Public.py_html import createHtml,relust
from Public.get_excel import datacel
from Public.Sendemail import send_email

'''执行测试的主要文件'''
def start_interface_html_http():
    starttime=datetime.datetime.now()
    day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir=os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '/test_case_data/case.xlsx'
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path)
    listrelust, list_fail, list_pass, list_json,list_exption,list_weizhi = testinterface()
    filepath =os.path.join(basdir+'/test_Report/%s-result.html'%day)
    
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime=datetime.datetime.now()
    
    createHtml(titles=u'http接口自动化测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust,weizhi=list_weizhi,exceptions=list_exption)
    
    #contec = u'http接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
    #list_pass, list_fail, list_exption, list_weizhi, filepath)
    
    contec = relust(titles=u'http接口自动化测试报告',starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relust=listrelust,weizhi=list_weizhi,exceptions=list_exption)
    
    send_email(contec,filepath)
    
if __name__ == '__main__':
    start_interface_html_http()