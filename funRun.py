from fun import  add
from fun import damage
from fun import print_student_files

if __name__=='__main__':
    """ add """
    # print(add(1,2))
    
    """damage """
    # print(type(damage(3,4)))
    # print(damage(3,4))

    # damage1,damage2=damage(3,4)
    # print(damage1,damage2)
    """print_student_files"""
    print_student_files('li','男',18,'人民路小学')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_student_files('yang')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_student_files('chen')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_student_files('du', '女', 16)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_student_files('au', '女', 16, collage='中国人大')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_student_files('cu',collage='中国人大')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_student_files('tiantian', collage='清华大学',age=19,gender='女')

