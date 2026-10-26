"""
KMP算法
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

def GetNext(t):
    m = t.length
    nextArray = [-1] * m  # 初始化nextArray[0]为-1，同时初始化nextArray数组大小是m
    for i in range(1, m):  # 求出next[1]~next[m-1]
        j = nextArray[i - 1]
        while j >= 0 and t.data[i] != t.data[j + 1]:
            j = nextArray[j]
        if (t.data[i] == t.data[j + 1]):
            nextArray[i] = j + 1
        else:
            nextArray[i] = -1
    return nextArray

# -1 -1 -1 0 1 2 3 -1 0 1
def PatternMatchKMP(s, t):
    if t.length == 0:
        return t
    if s.length == 0:
        return None
    nextArray = GetNext(t)
    i, j = 0, 0
    while i < s.length and j < t.length:
        if s.data[i] == t.data[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = nextArray[j - 1] + 1
    if j == t.length:
        return t
    return None

def main():
    s = ReadString()
    t = ReadString()
    p = PatternMatchKMP(s, t)
    if p == None:
        print('no match!')
    else:
        print('match')


main()