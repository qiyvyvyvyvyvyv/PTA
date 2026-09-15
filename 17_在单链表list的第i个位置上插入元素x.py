"""
要求实现一个函数，函数接收一个HeadNode类的对象list一个整数i和一个整数x。
函数在单链表list中的第i个位置插入给定的data=x的Node，
或者因为i为错误的插入位置(<1或>Length(list)+1)则输出position error并返回
"""
from asyncio.windows_events import NULL


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
    # print('----print linked list---')
    current_node = lst.head
    while current_node != None:
        print(current_node.data)
        current_node = current_node.next
    # print('----end---')


def Search(lst, x):
    current_node = lst.head
    while current_node != None and current_node.data != x:
        current_node = current_node.next
    return current_node


def Insert(lst, i, x):
    if i < 1 or i > Length(lst) + 1:
        print("position error")
        return
    nxt = lst.head
    node = Node(data=x)
    if nxt == None:
        lst.head = node
        return
    j = 1
    while nxt != None:
        if j == i - 1:
            node.next = nxt.next
            nxt.next = node
            return
        j += 1
        nxt = nxt.next

def main():
    n = int(input())
    lst = HeadNode()
    x = 0
    for i in range(1, n + 1):
        x = int(input())
        Insert(lst, i, x)
    PrintList(lst)
    Insert(lst, 0, x)
    Insert(lst, n + 2, x)
    PrintList(lst)


main()