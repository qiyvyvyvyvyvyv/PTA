"""
给定链表字符串类，本题要求实现一个能从原字符串的第pos个元素起截取len个字符作为新的字符串返回的函数
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

def SubString(s, pos, length):
    if pos < 1 or pos > s.length or length <= 0:
        return InitStr()
    if pos + length > s.length + 1:
        length = s.length - pos + 1
    sub_s = InitStr()
    p = s.head
    i = 1
    while i < pos:
        p = p.next
        i += 1
    q = None
    for _ in range(length):
        node = StringNode(p.data)
        if q is None:
            sub_s.head = node
        else:
            q.next = node
        q = node
        p = p.next
    sub_s.length = length
    return sub_s
# def SubString(s, pos, length):
#     if pos < 1 or pos > s.length or length < 0:
#         return StringNode()
#     if pos + length > s.length + 1:
#         length = s.length - pos + 1
#     sub_s = InitStr()
#     i = 1
#     p = s.head
#     while i < pos:
#         p = p.next
#         i += 1
#     num = 1
#     sub_s.head = p
#     p = p.next
#     q = sub_s.head
#     while num < length:
#         q.next = p
#         q = p
#         p = p.next
#         num += 1
#     q.next = None
#     sub_s.length = length
#     return sub_s

def main():
    s = ReadString()
    pos, length = map(int, input().split())
    sub_s = SubString(s, pos, length)
    PrintString(sub_s)


main()