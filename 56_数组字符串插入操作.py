"""
给定数组字符串类，本题要求实现一个能在字符串s中指定位置插入字符串t的函数。
如果字符数组长度因插入超过上限，则输出”error”
"""
kMaxSize = 1001

class StringNode:
    def __init__(self):
        self.data=['']*kMaxSize
        self.length=0

def InitStr():
    str = StringNode()
    return str

#算法4-1：字符串插入操作StrInsert(s, pos, t)
def StrInsert(s,pos,t):
    if s.length + t.length > kMaxSize or pos < 1 or pos > s.length + 1:
        print("error")
        return
    # range(13, 9, -1)
    # this is a test
    # 123456789abcedef
    # simple
    # 11
    for i in range(s.length - 1,pos - 2,-1):
        s.data[i + t.length] = s.data[i]
    for i in range(t.length):
        s.data[pos - 1 + i] = t.data[i]
    s.length += t.length
#算法4-1 结束

def ReadString():
    s = InitStr() #初始化StringNode类对象
    data = input()
    for i in range(len(data)):
        s.data[i] = data[i] #读入字符串
    s.length = len(data) #字符串的长度
    return s

def PrintString(s):
    for i in range(s.length):
        print(s.data[i],end='')

def main():
    s = ReadString()
    t = ReadString()
    pos = int(input())
    StrInsert(s, pos, t)
    PrintString(s)

main()