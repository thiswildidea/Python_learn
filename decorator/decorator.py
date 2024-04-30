import time

# def f1():
#     print('this is a function')

# def print_current_time(func):
#     print(time.time())
#     func()
    
# # print_current_time(f1)
# print(time.time())
# f1()


# 装饰器
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


@decorator
def f1():
    print('this is a function')
    
# f=decorator(f1)
# f()


f1()