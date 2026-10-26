"""
给定链表字符串类，本题要求实现一个能比较字符串s和t的函数。
比较规则：将原字符串与输入字符串t相比较，依次比较两字符串同位大小，
若相同则比较下一位，否则若原字符串大返回1，小返回-1，若等长部分全相同，则将原字符串较长返回1，较短返回-1，两字符串等长且相同返回0
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

def StrCompare(s, t):
    if s.length == 0 and t.length != 0:
        return -1
    if s.length != 0 and t.length == 0:
        return 1
    p, q = s.head, t.head
    while p != None and q != None:
        if p.data > q.data:
            return 1
        elif p.data < q.data:
            return -1
        else:
            p, q = p.next, q.next
    if p == None and q != None:
        return -1
    elif p != None and q == None:
        return 1
    else:
        return 0

def main():
    s = ReadString()
    t = ReadString()
    r = StrCompare(s, t)
    print(r)

main()