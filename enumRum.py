from em import VIP
if __name__=='__main__':
    # print(VIP.GREEN)
    # print(type(VIP.GREEN))
    
    # print(VIP.GREEN.name)
    # print(type(VIP.GREEN.name))
    
    # print(VIP['GREEN'])
    # print(type(VIP['GREEN']))
    
    # print(VIP.GREEN.value)
    
    # 循环遍历打印不会打印枚举标签的别名枚举
    # for v in VIP:
    #     print(v.name)
    
    # 循环遍历打印会打印枚举标签的别名枚举
    # for v in VIP.__members__:
    #     print(v)
    print(VIP(4))

