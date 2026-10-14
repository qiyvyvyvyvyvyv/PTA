"""
给定数组字符串类，本题要求实现一个能比较字符串s和t的函数。
比较规则：将原字符串与输入字符串t相比较，依次比较两字符串同位大小，若相同则比较下一位，
否则若原字符串大返回1，小返回-1，若等长部分全相同，则将原字符串较长返回1，较短返回-1，两字符串等长且相同返回0
"""
# 算法4-5：字符串比较操作  StrCompare(s,t)
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

def StrCompare(s, t):
    i, j = 0, 0
    while i < s.length and j < t.length:
        if s.data[i] > t.data[j]:
            return 1
        elif s.data[i] < t.data[j]:
            return -1
        else:
            i += 1
            j += 1
    if s.length == 0 and t.length == 0:
        return 0
    if s.length == 0:
        return -1
    if t.length == 0:
        return 1
    return s.length - t.length

def main():
    s = ReadString()
    t = ReadString()
    ret = StrCompare(s, t)
    print(ret)


main()