
#闭包=函数+环境变量
def curve_pre():
    # 环境变量，不能在下面函数中赋值
    a=25  
    def curve(x):
        return a*x*x
    return curve


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos=pos+step
        pos=new_pos
        return new_pos
    return go

