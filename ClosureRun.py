from  Closure import curve_pre
from Closure import factory
if __name__=='__main__':
    # f=curve_pre()
    # print(f.__closure__)
    # print(f.__closure__[0].cell_contents)
    # print(f(2))
    tourist = factory(0)
    print(tourist(2))
    print(tourist(3))
    print(tourist(5))
