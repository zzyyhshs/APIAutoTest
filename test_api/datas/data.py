# -*- coding: utf-8 -*-
# file: data.py
# author: zhuyao
# email: zzyyhshs@163.com

# 数据的存放格式以及方式都可以自己来指定
# 比如：xlrd读取excel里面的值
my_datas = {
    "test_address_add": {
        "uri": "/address/add",
        "body": {
                  "addressId": "string",
                  "city": "string",
                  "detail": "string",
                  "district": "string",
                  "mobile": "string",
                  "province": "string",
                  "receiver": "string",
                  "userId": "string"
                }
    },
    "test_address_delete": {
        "uri": "/address/delete",
        "userId": "2403129RFR1YK2NC",
        "addressId": "240315B13TM6651P"
    }
}

