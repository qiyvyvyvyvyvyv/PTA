"""
要求实现一个函数，函数接收一个HeadNode类的对象list和一个整数i。
函数删除单链表list中的第i个位置的Node，
或者因为i为错误的删除位置( <1或>Length(list) )则输出position error并返回
"""
# 2-8 不带头结点的单链表中的删除
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
    if i < 1:
        print('position error')
        return
    if i == 1:  # 插入第一个结点
        new_node = Node(x)
        lst.head = new_node
        lst.length = 1
    else:  # 寻找第i-1个结点并插入在其后面
        p = lst.head
        counter = 1
        while p != None and counter < i - 1:
            p = p.next
            counter += 1
        if p != None:  # 找到第i-1个位置
            new_node = Node(x)
            new_node.next = p.next
            p.next = new_node
        else:
            print('position error')


def Remove(list, i):
    if i < 1 or i > Length(list):
        print('position error')
        return
    nxt = list.head
    if i == 1:
        list.head = nxt.next
        return
    j = 1
    while j != i - 1 and nxt != None:
        nxt = nxt.next
        j += 1
    nxt.next = nxt.next.next

def main():
    lst = CreateList()
    i = int(input())
    Remove(lst, i)
    PrintList(lst)


main()
