"""
编号为1，2，3，...，n的n个人按照顺时针方向围坐一圈。
从第一个人开始按照顺时针方向从1开始报数，当报到指定的数m时，报m的人出列。
再从他顺时针方向的下一位人开始重新从1开始报数，报到m的人出列，如此下去，直到所有人都出列。
请设计算法用单向循环链表模拟约瑟夫问题的出列过程，输出出列的顺序
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def Attach(data, rear):
    rear.next = Node(data)
    rear = rear.next
    return rear

def JosephusProblem(n, m):
    head = Node(0)
    rear = head
    for i in range(1, n + 1):
        rear = Attach(i, rear)
    rear.next = head.next
    i = 1
    p = q = Node(0)
    rear = head.next
    last = head
    while head.next:
        if i % m == 0:
            if rear.data == head.next.data:
                # 如果出现要删除第一个节点的情况
                # 那么需要将头节点指向第一个节点的下一个节点
                head.next = head.next.next
            if rear.next == rear:
                # 最小规模问题
                # 如果只有一个节点, n < m
                # 我们的last是从头节点开始的
                # 这里直接置空会导致last.next是None出现异常
                # 因此只能使用continue提前结束当前循环
                head.next = None
                q = Attach(rear.data, q)
                continue
            q = Attach(rear.data, q)
            last.next = last.next.next
            rear = rear.next
        else:
            rear = rear.next
            last = last.next
        i += 1
    return p.next

if __name__ == '__main__':
    n, m = [int(i) for i in input().split()[:2]]
    result = JosephusProblem(n, m)

    # 打印出列的顺序
    current = result
    while current:
        print(current.data, end=" ")
        current = current.next