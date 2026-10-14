"""
给定数组字符串类，本题要求实现一个从原字符串的第pos个元素起删除len个字符的函数
"""
# 算法4-2：字符串删除操作StrRemove(s, pos, len)
kMaxSize = 1001

class StringNode:
    def __init__(self):
        self.data = [''] * kMaxSize
        self.length = 0


def InitStr():
    str = StringNode()
    return str

def StrInsert(s, pos, t):
    n = s.length
    m = t.length

    if pos < 1 or pos > n + 1 or (m + n) > kMaxSize:
        print("error")
        return s  # 错误，则不能插入，返回原字符串

    for i in range(n, pos - 1, -1):  # 将子串后移，给t留出空位
        s.data[i + m - 1] = s.data[i - 1]

    for i in range(m):
        s.data[pos - 1 + i] = t.data[i]  # 将t插入s
    s.length = n + m
    return s  # Python参数改变，需要返回

def ReadString():
    s = InitStr()  # 初始化StringNode类对象
    data = input()
    for i in range(len(data)):
        s.data[i] = data[i]  # 读入字符串
    s.length = len(data)  # 字符串的长度
    return s

def PrintString(s):
    for i in range(s.length):
        print(s.data[i], end='')

def StrRemove(s, pos, length):
    if pos < 1 or pos > s.length or length > s.length - pos + 1:
        return s
    # 9  14
    # this is a test
    # 0123456789abcd
    # 123456789abcde
    # 8 2
    for i in range(pos + length - 1, s.length):
        s.data[i - length] = s.data[i]
    s.length -= length
    return s

def main():
    s = ReadString()
    pos, length = map(int, input().split())
    StrRemove(s, pos, length)
    PrintString(s)


main()