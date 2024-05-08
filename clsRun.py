from cls import Student

# student = Student('王欢',30)
# student.do_homework()

#打印实例对象
# print(student.__dict__)

# 实例对象变量
# print(student.name)
# print(student.age)

# 打印类
# print(Student.__dict__)

# 类变量
# print(Student.name)
# print(Student.age)


#类方法调用
# student1 = Student('王欢',30)
# Student.plus_sum()
# student1.plus_sum()

# student2 = Student('王',20)
# Student.plus_sum()
# student2.plus_sum()

# student3 = Student('王dd', 20)
# Student.plus_sum()
# student3.plus_sum()

# 静态方法调用
# student4 = Student('王dd', 20)
# Student.add(1,2)
# student4.add(1,2)


# 调用私有实例变量和私有实例方法
# (调用私有实例变量)
# student = Student('王dd', 20)
# student._Student__score = 100
# print(student.__dict__)

# 调用私有实例方法
# student = Student('王dd', 20)
# student._Student__marking(99)
# print(Student.__dict__)


#类的继承
# student = Student('王dd',20)
# student.get_name()
# print(student.name)
# print(student.__dict__)
# print(student.do_homework())
