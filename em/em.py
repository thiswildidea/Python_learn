from enum import Enum
from enum import IntEnum,unique

@unique
class VIP_int(IntEnum):
    YELLOW=1
    YELLOW_ALIAS = 2
    GREEN=3
    BLACK=4
    RED=5


class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4
"""
枚举可以进行== 和is 运算，但是不可以进行> 比较运算

"""

"""
枚举标签不可以重复复，枚举值可以重复，如果枚举值相同
第二相同枚举值的标签最好改成第一个的别名，for 循环遍历打印不会打印枚举标签的别名枚举
"""
