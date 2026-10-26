"""
给定链表字符串类，本题要求实现一个能向原字符串pos位置起删除len个字符的函数
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

def StrRemove(s, pos, length):
    if pos < 1 or pos > s.length or length > s.length - pos + 1:
        return s
    pos -= 1
    i, num = 0, 0
    p = s.head
    if pos == 0:
        while num < length:
            s.head = s.head.next
            num += 1
    else:
        while i < pos - 1:
            i += 1
            p = p.next
        while num < length:
            p.next = p.next.next
            num += 1
    s.length -= length
    return s

def main():
    s = ReadString()
    pos, length = map(int, input().split())
    s = StrRemove(s, pos, length)
    PrintString(s)

main()