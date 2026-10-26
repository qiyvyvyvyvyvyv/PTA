"""
给定数组字符串类，本题要求实现一个能匹配字符串s和目标字符串t的函数。
若存在s的子串与t相同则认为匹配成功，返回该子串的头节点；否则认为匹配失败返回None
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

# abcdefgh
#     abbb
def PatternMatchBF(s, t):
    if t.length == 0:
        return t
    for i in range(s.length - t.length + 1):
        if s.data[i] == t.data[0]:
            j = 1
            while j < t.length and s.data[i + j] == t.data[j]:
                j += 1
            if j == t.length:
                return t
    return None

def main():
    s = ReadString()
    t = ReadString()
    p = PatternMatchBF(s, t)
    if p == None:
        print('no match!')
    else:
        print('match')


main()