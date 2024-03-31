# -*- coding: utf-8 -*-
# file: 5.request_cookie.py
# author: zhuyao
# email: zzyyhshs@163.com

import requests


url = "http://localhost:8088/myorders/trend?userId=2403129RFR1YK2NC&page=1&pageSize=5"
headers = dict()
headers["Content-Type"] = "application/json"
# cookie的第一种添加方式
# headers["Cookie"] = "user=%7B%22id%22%3A%222403129RFR1YK2NC%22%2C%22username%22%3A%22test12%22%2C%22password%22%3Anull%2C%22nickname%22%3A%22test12%22%2C%22realname%22%3Anull%2C%22face%22%3A%22http%3A%2F%2F122.152.205.72%3A88%2Fgroup1%2FM00%2F00%2F05%2FCpoxxFw_8_qAIlFXAAAcIhVPdSg994.png%22%2C%22mobile%22%3Anull%2C%22email%22%3Anull%2C%22sex%22%3A2%2C%22birthday%22%3Anull%2C%22createdTime%22%3Anull%2C%22updatedTime%22%3Anull%7D"
# 第二种方式设置cookie
cookies = dict()
cookies["user"] = "%7B%22id%22%3A%222403129RFR1YK2NC%22%2C%22username%22%3A%22test12%22%2C%22password%22%3Anull%2C%22nickname%22%3A%22test12%22%2C%22realname%22%3Anull%2C%22face%22%3A%22http%3A%2F%2F122.152.205.72%3A88%2Fgroup1%2FM00%2F00%2F05%2FCpoxxFw_8_qAIlFXAAAcIhVPdSg994.png%22%2C%22mobile%22%3Anull%2C%22email%22%3Anull%2C%22sex%22%3A2%2C%22birthday%22%3Anull%2C%22createdTime%22%3Anull%2C%22updatedTime%22%3Anull%7D"

# 设置请求超时时间为 5 秒
# 从请求发送到返回的响应时间超过了5秒
response = requests.post(url, headers=headers, cookies=cookies, timeout=0.1)

print(response.status_code)
print(response.text)

