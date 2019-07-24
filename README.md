自动化接口框架：

Autotest

        ----config                      
                ----init.py             初始化文件
                ----config.py           配置文件，包括baseurl,失败重试次数，邮件配置等
                
        ----Public                      公共方法
                ----init.py
                ----Sendemail.py        发送邮件
                ----log.py              日志
                ----test_requests.py    request 请求方法
                ----py_html.py          html文件生成
                ----panduan.py          调用case时，判断执行结果
                ----get_excel.py        获取excel中不同表格信息
                
                
        ----interface
                ----init.py
                ----testFengzhuang.py   测试方法封装