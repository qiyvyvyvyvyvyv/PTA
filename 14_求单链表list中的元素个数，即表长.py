"""
要求实现一个函数，
函数接收一个HeadNode类的对象list。
通过遍历得到单链表list的长度并返回该长度
"""


# 2-4-1 求不带头结点的单链表的表长
class Node:
    def __init__(self, data=None, nxt=None):  # 参数nxt避免和关键字next重复
        self.data = data
        self.next = nxt


class HeadNode:
    def __init__(self, head_node=None, length=0):
        self.head = head_node
        self.length = length


def Length(lst):
    nxt = lst.head
    length = 0
    while nxt != None:
        nxt = nxt.next
        length += 1
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


def main():
    lst = CreateList()
    # PrintList(lst)
    print(Length(lst))


main()