"""
如果用一个循环数组表示队列，且只有一个队列头指针front，不设队列尾指针rear，
而设置计数器count用以记录队列中结点的个数。请编写算法实现队列的三个基本运算：判空、入队、出队。
当调用 EnQueue 但队列已满，或调用 DeQueue 但队列为空时，应该在一行中输出错误信息 ERROR
"""
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.count = 0
        self.data = [None] * capacity

def IsEmpty(queue):
    if queue.count == 0:
        return True
    else:
        return False

def EnQueue(queue, x):
    if queue.count == queue.capacity:
        print("ERROR")
        return
    rear = (queue.front + queue.count) % queue.capacity
    queue.data[rear] = x
    queue.count += 1

def DeQueue(queue):
    if queue.count == 0:
        print("ERROR")
        return
    num = queue.data[queue.front]
    queue.front = (queue.front + 1) % queue.capacity
    queue.count -= 1
    print(num)

def main():
    queue_capacity = int(input())  # 从输入中获取队列容量
    my_queue = Queue(queue_capacity)

    while True:
        operation = input().split()

        if operation[0] == 'I':
            EnQueue(my_queue, int(operation[1]))
        elif operation[0] == 'O':
            DeQueue(my_queue)
        elif operation[0] == 'E':
            break
main()