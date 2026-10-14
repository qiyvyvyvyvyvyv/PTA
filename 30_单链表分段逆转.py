"""
给定一个带头结点的单链表和一个整数k，
要求你将链表中的每k个结点做一次逆转。
例如给定单链表 1→2→3→4→5→6 和 k = 3，
你需要将链表改造成 3→2→1→6→5→4；如
果 k = 4，则应该得到 4→3→2→1→5→6
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def K_Reverse(linkedlist, k):
    n = 0
    p = linkedlist
    while p:
        n += 1
        p = p.next
    end = n // k * k
    p = linkedlist
    head = Node(0)
    rear = q = head
    i = 0
    while p is not None:
        if i < end:
            if i % k == 0:
                rear = q
                q = Node(p.data)
                rear.next = q
                p = p.next
                i += 1
            else:
                node = Node(p.data)
                node.next = rear.next
                rear.next = node
                p = p.next
                i += 1
        else:
            q.next = p
            break
    return head.next



if __name__ == '__main__':
    length = int(input())
    nodes_data = list(map(int, input().split()))

    # 创建带头结点的单链表
    linkedlist = Node()
    current = linkedlist
    for data in nodes_data:
        current.next = Node(data)
        current = current.next

    # 设置k值
    k = int(input())

    # 调用逆转函数
    result = K_Reverse(linkedlist.next, k)

    # 打印逆转后的链表
    current = result
    while current:
        print(current.data, end=" ")
        current = current.next