"""
给定数组字符串类和算法4-1~2、11所写的字符串插入、删除、朴素匹配算法，
本题要求实现一个能将s字符串中的subStr子串替换为t字符串，若s字符串中无subStr子串，则不做处理的函数
"""
kMaxSize = 1001
class StringNode:
    def __init__(self):
        self.data = [''] * kMaxSize
        self.length = 0

def InitStr():
    str = StringNode()
    return str

# 算法4-1：字符串插入操作StrInsert(s, pos, t)
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
# 算法4-1 结束

# 算法4-2：字符串删除操作StrRemove(s, pos, len)
def StrRemove(s, pos, length):
    n = s.length
    if (pos + length - 1) <= n:  # 从待删除位置到Length后面还有串拷贝到前面
        for i in range(pos + length - 1, n + 1):  # i=n处理结束符
            s.data[i - length] = s.data[i]
        s.length = n - length
    else:  # 需要将从数组下标pos-1开始的所有字符都删掉
        s.length = pos - 1
    return s

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

def PatternMatchBF(s, t):
    n = s.length
    m = t.length
    p = 0
    while p < n - m + 1:
        i = 0
        while i < m:
            if s.data[p + i] != t.data[i]:
                break  # 不匹配则从下一个位置p开始
            i += 1
        if i == m:
            break
        p += 1
    if p > n - m:  # 匹配不成功
        p = None
    return p


# 算法 4-12：字符串替换算法  Replace(s, sub_s, t)
def Replace(s, sub_s, t):
    if sub_s.length == 0:
        return None
    if t.length == 0:
        return None
    if s.length == 0:
        return None
    while True:
        pos = PatternMatchBF(s, sub_s)
        if pos != None:
            s = StrRemove(s, pos + 1, sub_s.length)
            s = StrInsert(s, pos + 1, t)
        else:
            break
    return s

def main():
    s = ReadString()
    sub_s = ReadString()
    t = ReadString()
    Replace(s, sub_s, t)
    PrintString(s)


main()