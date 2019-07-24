#!usr/bin/python3
# -*-coding:utf-8 -*-

import sys
sys.path.append('..')

from email.mime.text import MIMEText
from email.mime.nonmultipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
from config.config import From_addr,Password,To_addrs,Smtp_server
import time

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))


def send_email(contents,Enclosure):
    from_addr = From_addr
    password = Password
    to_addrs = To_addrs
    smtp_server = Smtp_server
    
    day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    msg = MIMEMultipart()
    msg['From'] = _format_addr('汪庆<%s>' % from_addr)
    msg['To'] = _format_addr('研发组<%s>' % to_addrs)
    msg['Subject'] = Header('EC接口自动化测试报告%s' % day,'utf-8').encode()   
    msg.attach(MIMEText(contents,'html','utf-8'))

    with open(Enclosure,'rb') as f:
        mime = MIMEBase('html','html',filename='EC接口自动化测试报告.html')
        mime.add_header('Content-Disposition', 'attachment', filename='EC接口自动化测试报告.html')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')  
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)    
        
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr, [to_addrs], msg.as_string())
    server.quit()

