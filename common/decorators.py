# -*- coding: utf-8 -*-
# file: decorators.py
# author: zhuyao
# email: zzyyhshs@163.com


from functools import wraps

from config import logger

'''
封装 ui 接口 公用的装饰器

需求： 
1. 用例执行成功  ： 需要记录 用例的参数， 执行是否成功  pass
2. 用例执行失败 ： 也需要记录 用例的参数， 执行是否成功 fail
'''
def logs(fn):
    @wraps(fn)
    def wrapper_function(*args , **kwargs):
        try:
            fn(*args , **kwargs) # 执行测试用例
            # 记录： 测试用例的名字 ，参数 ：   执行结果：
            logger.info(msg=f"{fn.__name__} , *tuple：{args} , **kw : {kwargs}" ,extra={"status" : "pass"})
        except Exception:
            logger.exception(msg=f"{fn.__name__} , *tuple：{args} , **kw : {kwargs}" ,extra={"status" : "fail"} ,exc_info=True)
            raise

    return wrapper_function

