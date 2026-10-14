"""
给出链式队列节点类和链式队列类的定义，要求实现三个函数(类方法)，
分别实现对自定义链式队列类的EnQueue、GetFront和DeQueue操作。
EnQueue函数接收一个数据x，函数将x加入队尾。
GetFront函数若队列为空则报错，输出”Queue is empty”，并返回None，否则返回队首数据。
DeQueue函数若队列为空则报错，输出”Queue is empty”，否则将原队首出队。
"""
class QueueNode:
    def __init__(self, data):
        self.data = data  # 存储数据
        self.next = None  # 链式队列中下一个元素的位置


class Queue:
    def __init__(self):
        self.size = 0  # 链式队列中当前元素个数
        self.front = None  # 链式队列的队首指针，初始化为None
        self.rear = None  # 链式队列的队尾指针，初始化为None


def InitQueue():
    queue = Queue()
    return queue


def IsEmpty(queue):
    return queue.size == 0

# 算法3-9：链接队列的销毁操作 DestroyQueue(queue)
def DestroyQueue(queue):
    queue = None

# 算法3-9：链接队列的销毁操作 DestroyQueue(queue) 结束

# 算法3-10：链接队列的入队操作 EnQueue(queue, x)

def EnQueue(self, x):
    if self.rear is None:
        self.rear = QueueNode(x)
        self.front = self.rear
        self.size += 1
    else:
        self.rear.next = QueueNode(x)
        self.rear = self.rear.next
        self.size += 1
# 算法3-10 结束

# 算法3-11：链接队列的查看队首操作 GetFront(queue)


def GetFront(self):
    if IsEmpty(self):
        print("Queue is empty")
        return None
    else:
        return self.front.data

# 算法3-11 结束

# 算法3-12：链接队列的出队操作 DeQueue(queue)


def DeQueue(self):
    if IsEmpty(self):
        print("Queue is empty")
    else:
        self.front = self.front.next
        self.size -= 1

 # 算法3-12 结束


def main():
    n = int(input())
    queue = Queue()
    for i in range(n):
        x = int(input())
        EnQueue(queue, x)
    for i in range(n + 1):  # 最后一个操作用于测试队列空报错
        print(GetFront(queue))
        DeQueue(queue)
    DestroyQueue(queue)


main()