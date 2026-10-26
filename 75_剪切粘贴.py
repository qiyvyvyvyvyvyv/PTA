"""
使用计算机进行文本编辑时常见的功能是剪切功能（快捷键：Ctrl + X）。请实现一个简单的具有剪切和粘贴功能的文本编辑工具。
工具需要完成一系列剪切后粘贴的操作，每次操作分为两步：
· 剪切：给定需操作的起始位置和结束位置，将当前字符串中起始位置到结束位置部分的字符串放入剪贴板中，
并删除当前字符串对应位置的内容。例如，当前字符串为 abcdefg，起始位置为 3，结束位置为 5，则剪贴操作后，
剪贴板内容为 cde，操作后字符串变为 abfg。字符串位置从 1 开始编号。
· 粘贴：给定插入位置的前后字符串，寻找到插入位置，将剪贴板内容插入到位置中，
并清除剪贴板内容。例如，对于上面操作后的结果，给定插入位置前为 bf，插入位置后为 g，则插入后变为 abfcdeg。
如找不到应该插入的位置，则直接将插入位置设置为字符串最后，仍然完成插入操作。查找字符串时区分大小写。
每次操作后的字符串即为新的当前字符串。在若干次操作后，请给出最后的编辑结果
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

def SubString(s, pos, length):
    if pos < 1 or pos > s.length or length < 0 or pos + length > s.length + 1:
        return InitStr()
    sub_s = InitStr()
    for i in range(length):
        sub_s.data[i] = s.data[pos - 1 + i]
    sub_s.length = length
    return sub_s

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
        return i - t.length
    return -1

def main():
    s = ReadString()
    n = int(input())
    for _ in range(n):
        op = input().split()
        start = int(op[0])
        end = int(op[1])
        sub_str = SubString(s, start, end - start + 1)
        StrRemove(s, start, end - start + 1)
        if s.length == 0:
            StrInsert(s, 1, sub_str)
            continue
        t = InitStr()
        t.data = ''.join(op[2:])
        t.length = len(''.join(op[2:]))
        index = PatternMatchKMP(s, t)
        if index != -1:
            StrInsert(s, index + len(op[2]) + 1, sub_str)
        else:
            StrInsert(s, s.length + 1, sub_str)
    PrintString(s)

main()