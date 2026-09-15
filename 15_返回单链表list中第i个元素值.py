"""
要求实现一个函数，
函数接收一个HeadNode类的对象list和一个整数i。
函数通过遍历得到单链表list第i个元素值或因链表不存在第i个元素而返回None
"""


# 2-5 返回不带头结点的单链表中第i个元素值
# 2-6 不带头结点的单链表中的查找
class Node:
    def __init__(self, data=None, nxt=None):  # 参数nxt避免和关键字next重复
        self.data = data
        self.next = nxt


class HeadNode:
    def __init__(self, head_node=None, length=0):
        self.head = head_node
        self.length = length


def Length(lst):
    current_node = lst.head
    length = 0
    while current_node != None:
        length += 1
        current_node = current_node.next
    return length


def CreateList():
    n = int(input())
    lst = HeadNode()  # 头结点,数据为缺省值None
    for i in range(n):
        x = int(input())  # 假设数据类型是整数
        new_node = Node(x)
        if i == 0:
            current_node = lst.head = new_node
        else:
            current_node.next = new_node
            current_node = current_node.next
    return lst


def PrintList(lst):
    print('----print linked list---')
    current_node = lst.head
    while current_node != None:
        print(current_node.data)
        current_node = current_node.next
    print('----end---')


def Search(lst,x):
    nxt = lst.head
    while nxt != None:
        if nxt.data == x:
            return nxt
        nxt = nxt.next
    return None


def main():
    lst = CreateList()
    x = int(input())
    p = Search(lst, x)
    if p != None:
        print(p.data)
    else:
        print(x, 'is not found!')


main()