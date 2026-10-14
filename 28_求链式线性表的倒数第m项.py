"""
设计时间和空间上都尽可能高效的算法，求链式存储的线性表的倒数第m个元素。
函数Find的功能是，返回带空头结点的单链表linkedlist的倒数第m个元素的值，并且不得对linkedlist做任何改变。
如果这样的元素不存在，则返回一个错误字符串“ERROR”
"""
class ListNode:
    def __init__(self, data, position=None):
        self.data = data
        self.next = position

def Find(linkedlist, m):
    if linkedlist is None:
        return "ERROR"
    p = q = linkedlist
    i = 1
    while p.next is not None:
        if i < m:
            p = p.next
            i += 1
        else:
            p = p.next
            q = q.next
            i += 1
    if i < m:
        return "ERROR"
    return q.data

if __name__ == '__main__':
    m = int(input())
    data = list(map(int, input().split()))
    linkedlist = None
    current_node = None

    # 构建链表
    for value in data:
        if not linkedlist:
            linkedlist = ListNode(value)
            current_node = linkedlist
        else:
            current_node.next = ListNode(value)
            current_node = current_node.next

    # 调用函数并输出结果
    result = Find(linkedlist, m)
    print(result)