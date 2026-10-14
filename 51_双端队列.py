"""
双端队列（deque，即double-ended queue的缩写）是一种具有队列和栈性质的数据结构，
即可以（也只能）在线性表的两端进行插入和删除。队列数组中保留一个多余的空位以区分队列的满和空状态
EnQueue(deque, x)：将元素x插入到双端队列deque的头；
DeQueue(deque)：删除双端队列deque的头元素，并返回其值；
Inject(deque, x)：将元素x插入到双端队列deque的尾部；
Eject(deque)：删除双端队列deque的尾部元素，并返回其值。
EnQueue和Inject应该在正常执行完操作后返回true，或者在队满时返回false。
当front和rear相等时队列为空，DeQueue和Eject必须返回由裁判程序定义的ERROR
"""
class DequeNode:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.data = [None] * (capacity + 1)

def is_empty(deque):
    return deque.front == deque.rear

def is_full(deque):
    return (deque.rear + 1) % (deque.capacity + 1) == deque.front

def EnQueue(deque, x):
    # 头部插入
    if not is_full(deque):
        deque.data[deque.front] = x
        deque.front = (deque.front - 1) % (deque.capacity + 1)
        return True
    else:
        print("Deque is Full!")
        return False

def Eject(deque):
    # 尾部删除
    if not is_empty(deque):
        x = deque.data[deque.rear]
        deque.data[deque.rear] = None
        deque.rear = (deque.rear - 1) % (deque.capacity + 1)
        return x
    else:
        print("Deque is Empty!")
        return False

def DeQueue(deque):
    # 头部删除
    if not is_empty(deque):
        deque.front = (deque.front + 1) % (deque.capacity + 1)
        x = deque.data[deque.front]
        deque.data[deque.front] = None
        return x
    else:
        print("Deque is Empty!")
        return False

def Inject(deque, x):
    # 尾部插入
    if not is_full(deque):
        deque.rear = (deque.rear + 1) % (deque.capacity + 1)
        deque.data[deque.rear] = x
        return True
    else:
        print("Deque is Full!")
        return False

if __name__ == '__main__':
    # 示例输入
    n = int(input())
    deque = DequeNode(n)

    # 测试用例
    while True:
        command = input().split()
        if command[0] == "End":
            break
        elif command[0] == "EnQueue":
            result = EnQueue(deque, int(command[1]))
        elif command[0] == "DeQueue":
            result = DeQueue(deque)
            if result :
                print(f"{result} is out")
        elif command[0] == "Inject":
            result = Inject(deque, int(command[1]))
        elif command[0] == "Eject":
            result = Eject(deque)
            if result:
                print(f"{result} is out")
    print("Inside Deque:", end="")
    # 打印剩余元素
    while not is_empty(deque):
        result = DeQueue(deque)
        if result :
            print(result, end=' ')
