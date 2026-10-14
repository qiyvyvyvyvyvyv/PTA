"""
给定数组字符串类，本题要求实现一个能从原字符串的第pos个元素起截取len个字符作为新的字符串返回的函数
"""
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

def SubString(s, pos, length):
    # if pos < 1 or pos > s.length or length < 0 or pos + length > s.length + 1:
    #     print("error")
    #     return InitStr()
    sub_s = InitStr()
    for i in range(length):
        sub_s.data[i] = s.data[pos - 1 + i]
    sub_s.length = length
    return sub_s

def main():
    s = ReadString()
    pos, length = map(int, input().split())
    sub_s = SubString(s, pos, length)
    PrintString(sub_s)


main()