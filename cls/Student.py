"""
2024.04.24
面向对象
有意义的面向对象的代码
类=面向对象
类、对象
实例化
类最基本的作用:封装
__init__() should return None ,not 'str'
"""

"""
 构造函数(特殊的实例方法),实例化时候自动调用,没有返回值
"""

"""
类变量访问 self.__class__.sum 
实例对象变量
self 显胜于隐 只和对象有关系和类没关系
cls  只和类有关系和对象没关系
"""
from cls  import Human

class Student(Human):
    # 类变量
    sum=0
    name='学生'
    age=10
    def __init__(self,name,age):
     # 实例对象变量
        super().__init__(name,age)
        # self.name=name
        # self.age=age
        self.school='清华大学'
        self.__score = 0
     #访问类变量
        self.__class__.sum =10
     #实例方法  
    def do_homework(self):
        print('homework')
        self.__do_english_homework()
        
    def __do_english_homework(self):
        print('english work')
    
    def __marking(self,score):
        self.__score = score
        print(self.name+'同学本次考试分数为：'+str(self.__score))
        
    def get_name(self):
        super().get_name()
        print("111")
    #类方法
    @classmethod
    def plus_sum(cls):
        cls.sum+=1
        print(cls.sum)
        
    # 静态方法（不建议用）
    @staticmethod
    def add(x,y):
        Student.sum+=1
        print('this is a static method')
