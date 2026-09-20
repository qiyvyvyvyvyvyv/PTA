"""
链表采用带空头结点的方式实现，
请修改算法2-7（单链表插入）和算法2-8（单链表删除），实现相应的插入和删除操作
其中单链表结构List的定义与代码2-4中相同，不再赘述；i是元素x需要被插入或删除的位序（从1开始）。
若传入的位序i不是合理的位置，则在一行中打印“ERROR”。
注意：list的头指针head指向一个空的头结点，这个结点里不存任何真实数据
"""
class Node():
    def __init__(self, data=None, next=None) -> None:
        self.data = data  # 储存数据             类型: int
        self.next = next  # 指向下一个ListNode   类型: ListNode


class HeadNode():
    def __init__(self, head, length) -> None:
        self.head = head  # 指向第一个ListNode 类型: ListNode
        self.length = length  # 链表长度           类型: int


def Insert(linkedlist, i, x):
    if i < 1 or i > linkedlist.length + 1:
        print("ERROR")
        return
    if i == 1:
        new_node = Node(x)
        new_node.next = linkedlist.head.next
        linkedlist.head.next = new_node
        linkedlist.length += 1
    else:
        p = linkedlist.head
        for _ in range(i - 1):
            p = p.next
        new_node = Node(x)
        new_node.next = p.next
        p.next = new_node
        linkedlist.length += 1

def Remove(linkedlist, i):
    if i < 1 or i > linkedlist.length:
        print("ERROR")
        return
    if i == 1:
        p = linkedlist.head
        linkedlist.head = p.next
        linkedlist.length -= 1
    else:
        p = linkedlist.head
        for _ in range(i - 1):
            p = p.next
        p.next = p.next.next
        linkedlist.length -= 1

if __name__ == '__main__':
    tmpList = [int(i) for i in input().split()]
    flag, i, x = [int(i) for i in input().split()[:3]]
    linkedlist = HeadNode(Node(None, None), 0)
    for n in range(len(tmpList), 0, -1):
        Insert(linkedlist, 1, tmpList[n - 1])
    if flag == 0:
        Insert(linkedlist, i, x)
    else:
        Remove(linkedlist, i)
    tmp = linkedlist.head.next
    while tmp != None:
        print(tmp.data, end=" ")
        tmp = tmp.next