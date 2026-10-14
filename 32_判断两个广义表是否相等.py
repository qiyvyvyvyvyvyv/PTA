"""
判断两个广义表是否相等
"""
class GListNode:
    def __init__(self, tag, data=None, sub_list=None):
        self.tag = tag
        self.data = data
        self.sub_list = sub_list
        self.next = None

class GList:
    def __init__(self):
        self.head = None

def init_g_list(glist):
    glist.head = GListNode('head')
    p = glist.head
    data = [i for i in input().split()]
    for i in data:
        if i.isdigit():
            p.next = GListNode('data', int(i), None)
        else:
            p.next = GListNode('sublist', None, init_g_list(GList()))
        p = p.next
    glist.head = glist.head.next
    return glist

def IsEqual(glist1, glist2):
    p1 = glist1.head
    p2 = glist2.head
    while p1 and p2:
        if p1.tag != p2.tag or p1.data != p2.data:
            return False
        if p1.tag == 'data':
            p1 = p1.next
            p2 = p2.next
        else:
            if not IsEqual(p1.sub_list, p2.sub_list):
                return False
            p1 = p1.next
            p2 = p2.next
    return p1 is None and p2 is None

if __name__ == '__main__':
    glist1 = init_g_list(GList())
    glist2 = init_g_list(GList())

    result = IsEqual(glist1, glist2)
    print(result)
