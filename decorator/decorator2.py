import time

# 装饰器
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f1(func_name):
    print('this is a function named'+func_name)
    

@decorator
def f2(func_name, func_name1):
    print('this is a function named'+func_name)
    print('this is a function named'+func_name1)


@decorator
def f3(func_name, func_name1,**kw):
    print('this is a function named'+func_name)
    print('this is a function named'+func_name1)
    print(kw)
f3('func_name', 'func_name1',a=1,b=1,c=1,d='dddddd')
