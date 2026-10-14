"""
给出顺序队列类的定义，要求实现三个函数(类方法)，分别实现对自定义顺序队列类的EnQueue、GetFront和DeQueue操作。
EnQueue函数接收一个数据x，若队列已满则报错，输出”Queue is full”，否则函数将x加入队尾。
GetFront函数若队列为空则报错，输出”Queue is empty”，并返回None，否则返回队首数据。
DeQueue函数若队列为空则报错，输出”Queue is empty”，否则将原队首出队
"""
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity  # 顺序队列的容量
        self.front = 0  # 顺序队列的队首指针，初始化为0
        self.rear = 0  # 顺序队列的队尾指针，初始化为0
        self.data = [None] * capacity  # 存储数据的列表


def InitQueue(capacity):
    queue = Queue(capacity)
    return queue


def IsFull(queue):
    return (queue.rear + 1) % queue.capacity == queue.front


def IsEmpty(queue):
    return queue.front == queue.rear


# 算法3-7：顺序队列的入队操作 EnQueue(queue, x)
def EnQueue(queue, x):
    if IsFull(queue):
        print("Queue is full")
    else:
        queue.data[queue.rear] = x
        queue.rear = (queue.rear + 1) % queue.capacity


# 算法3-7 结束

# 算法3-8：顺序队列的查看队首操作 GetFront(queue)
def GetFront(queue):
    if IsEmpty(queue):
        print("Queue is empty")
        return None
    else:
        return queue.data[queue.front]


# 算法3-8 结束

# 算法3-9：顺序队列的出队操作 DeQueue(queue)
def DeQueue(queue):
    if IsEmpty(queue):
        print("Queue is empty")
    else:
        q = queue.data[queue.front]
        queue.front = (queue.front + 1) % queue.capacity
        return q


# 算法3-9 结束

def DestroyQueue(queue):
    del queue


def main():
    n = int(input())
    queue = Queue(n + 1)
    for i in range(n + 1):  # 最后一个输入用于测试队列满报错
        x = int(input())
        EnQueue(queue, x)
    for i in range(n + 1):  # 最后一个操作用于测试队列空报错
        print(GetFront(queue))
        DeQueue(queue)
    DestroyQueue(queue)


main()