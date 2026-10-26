"""
给定链表字符串类，本题要求实现一个能向原字符串pos位置插入新字符串t的函数。
如果插入位置合法，返回拼接后的字符串，如果插入位置不合法，则输出”position error”，返回拼接前的s字符串
"""
# 算法4-6 链式存储的字符串的插入操作
NormalCode = 0
ErrorCode = 1


class StringNode:
    def __init__(self, data='', next=None):
        self.data = data
        self.next = next

class StringHeadNode:
    def __init__(self):
        self.head = StringNode()
        self.length = 0

def InitStr():
    s = StringHeadNode()
    return s

def StrInsert(s, pos, t):
    if pos < 1 or pos > s.length + 1:
        print("position error")
        return s
    if t.length == 0:
        return s
    q = None
    if pos == 1:
        q = s.head
        s.head = t.head
    else:
        pos -= 2
        i = 0
        p = s.head
        while i < pos:
            p = p.next
            i += 1
        q = p.next
        p.next = t.head
    i = 0
    p = t.head
    while i < t.length - 1:
        p = p.next
        i += 1
    p.next = q
    s.length += t.length
    return s

def ReadString():
    s = InitStr()
    tail = s.head
    data = input()
    for d in data:
        tail.next = StringNode(d)
        tail = tail.next
        s.length += 1
    tail.next = None
    tail = s.head
    s.head = s.head.next
    return s

def PrintString(s):
    p = s.head
    while p != None:
        print(p.data, end='')
        p = p.next

def main():
    s = ReadString()
    t = ReadString()
    pos = int(input())
    s = StrInsert(s, pos, t)
    PrintString(s)


main()