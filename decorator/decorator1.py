import time

# 装饰器
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper


@decorator
def f1(func_name):
    print('this is a function named'+func_name)
    

@decorator
def f2(func_name, func_name1):
    print('this is a function named'+func_name)
    print('this is a function named'+func_name1)


f2('func_name', 'func_name1')
