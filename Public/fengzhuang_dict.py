#!usr/env/bin python3
# -*- coding: utf-8 -*-

# @Time    : 2019/7/23 20:36
# @Author  : wq
# @File    : Fengzhuang_dict.py

'''字典取值'''
def res(d,code):
    
    result=[]
    if isinstance(d, dict) and code in d.keys():
        value = d[code]
        result.append(str(value))
        return result
    
    elif isinstance(d, (list, tuple)):
            for item in d:
                value=res(item,code)
                if value =="None" or value is None:
                    pass
                elif len(value)==0:
                    pass
                else:
                    result.append(value)
            return result
    else:
        if isinstance(d, dict):
            for k in d:
                value=res(d[k], code)
                if value =="None" or value is None :
                    pass
                elif len(value)==0:
                    pass
                else:
                    for item in value:
                        result.append(item)
            return result

if __name__ == "__main__":
    d = {'code': 0, 'result': '{"redirect":"https://www.uat.art2print.cn"}'}
    code = 'code'
    res(d, code)