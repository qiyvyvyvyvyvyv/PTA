"""
给定链表字符串类，本题要求实现一个能在原字符串的末尾连接加入新字符串t的函数
"""
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
    flag = NormalCode
    if t.length > 0:  # 若t不是空串
        tail = t.head
        while tail.next != None:  # 找到t的最后一个元素
            tail = tail.next
        if s.length > 0:  # 若s不是空串
            p = s.head
            count = 1
            while p != None and count < pos - 1:
                # 找第pos个元素的前一个元素
                count += 1
                p = p.next
            if count == pos - 1:  # 将t插在p的后面
                tail.next = p.next
                p.next = t.head
            elif pos == 1:  # t插在s的头
                tail.next = s.head
                s.head = t.head
            else:
                print('position error')
                flag = ErrorCode
        else:  # 若s是空串
            s = t
    if flag != ErrorCode:
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

def StrConcat(s, t):
    if s.length == 0 and t.length != 0:
        return t
    if s.length != 0 and t.length == 0:
        return s
    p = s.head
    while p.next != None:
        p = p.next
    p.next = t.head
    s.length += t.length
    return s

def main():
    s = ReadString()
    t = ReadString()
    s = StrConcat(s, t)
    PrintString(s)


main()