"""
现有两个带头结点的单链表logList1和logList2，分别存储两组系统日志。
每个链表的节点包含时间戳（整数，代表日志产生时间） 和日志内容（字符串），
且两个链表均已按时间戳升序排列（时间戳越小，日志产生越早）。
请设计算法，将两个链表合并为一个新的带头结点单链表，要求：
新链表仍按时间戳升序排列；
若两日志时间戳相同，保持logList1中的日志在logList2中的日志之前；
合并过程中仅通过修改节点的指针（或引用）完成拼接，
不允许复制节点数据或创建新节点（仅可创建一个新的头结点作为合并后链表的起点）。
例如：
logList1节点序列（时间戳）：100 → 300 → 500
logList2节点序列（时间戳）：200 → 300 → 600
合并后节点序列（时间戳）：100 → 200 → 300 → 300 → 500 → 600
"""
class ListNode:
    def __init__(self):
        self.head = Node(0)
        self.length = 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def readList():
    lst = ListNode()  # 带头结点的链表
    rear = lst.head  # 尾指针，初始指向头结点
    for x in map(int, input().split()):
        if x == -1:  # 遇到结束标志，本链表读完
            break
        rear.next = Node(x)  # 尾插
        rear = rear.next
        lst.length += 1
    return lst

def PrintList(lst):
    p = lst.head.next
    i = 0
    while p is not None:
        i += 1
        if i != lst.length:
            print(p.data, end=' ')
        else:
            print(p.data)
        p = p.next

def main():
    logList1 = readList()
    logList2 = readList()
    if logList1.length == 0:
        PrintList(logList2)
        return
    if logList2.length == 0:
        PrintList(logList1)
        return
    list = ListNode()
    rear = list.head
    list1_rear = logList1.head.next
    list2_rear = logList2.head.next
    while list1_rear is not None and list2_rear is not None:
        if list1_rear.data < list2_rear.data:
            rear.next = list1_rear
            list1_rear = list1_rear.next
            list.length += 1
        else:
            rear.next = list2_rear
            list2_rear = list2_rear.next
            list.length += 1
        rear = rear.next
    if list1_rear is not None:
        rear.next = list1_rear
        list.length += 1
    if list2_rear is not None:
        rear.next = list2_rear
        list.length += 1
    PrintList(list)

if __name__ == "__main__":
    main()