def add(a, b):
    return a+b

def damage(skill1,skill2):
    damage1 =skill1*3
    damage2=skill2*2+10
    return damage1,damage2


"""
参数
1.必须参数（按照顺序赋值）
2.关键字参数（按照关键字）
3.默认参数
"""
def print_student_files(name,gender='男',age=18,collage='人民路小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print('我在'+collage+'上学')


