# -*- coding: utf-8 -*-
# file: my_common.py
# author: zhuyao
# email: zzyyhshs@163.com


class Connection:
    def __init__(self):
        print("创建链接")

    def close(self):
        print("关闭链接")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("获取用户信息")

    @property
    def is_authenticated(self):
        if self.username == "testuser" and self.password == "password1234":
            return True
        return False


def authenticate(username, password):
    return User(username, password)
