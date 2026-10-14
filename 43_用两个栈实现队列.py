"""
一个队列（先进先出结构）可以用两个堆栈（后进先出结构）来实现，方法如下：
从两个空堆栈s1和s2开始。
当元素 e 入队时，它实际上是被推入到s1。
当我们需要出队时，首先检查s2。如果s2是空的，
则把s1中的元素全部导入s2，即将每个元素从s1弹出后马上推入s2。
然后从s2中弹出元素 ——s2顶端元素一定是第一个进入s1的，所以是应该出列的第一个元素。
假设每个堆栈的推入和弹出操作都用 1 个单位时间，请你给出每个出队操作所花的时间
"""
class Stack():
    def __init__(self, kSize):    # 初始化一个大小为kSize的顺序栈
        self.capacity = kSize     # 顺序栈的容量
        self.top = -1             # 顺序栈的栈顶指针
        self.data = [None] * kSize        # 储存数据的数组

def init_stack(stack, kSize):
    stack.capacity = kSize
    stack.top = -1
    stack.data = [None] * kSize

def is_full(stack):             # 判断栈是否已满
    return stack.top+1 == stack.capacity

def is_empty(stack):            # 判断栈是否为空
    return stack.top == -1

def push(stack, x):
    if is_full(stack) :
        print("错误：栈已满。")
    else:
        stack.top += 1
        stack.data[stack.top] = x

def top(stack):
    if is_empty(stack):
        print("错误：栈为空。")
        return None
    else:
        return stack.data[stack.top]

def pop(stack):
    if is_empty(stack):
        print("错误：栈为空。")
    else:
        stack.top -= 1

def destroy_stack(stack):
    del stack

class Queue:
    def __init__(self):
        self.s1 = Stack(0)
        self.s2 = Stack(0)

class DeQElem:
    def __init__(self):
        self.x = 0
        self.time = 0

def init_queue(queue, size):
    init_stack(queue.s1, size)
    init_stack(queue.s2, size)

def en_queue(queue, x):
    stack = queue.s1
    if is_full(stack):
        print("错误：栈已满。")
        return
    push(stack, x)

def is_q_empty(queue):
    return is_empty(queue.s2) and is_empty(queue.s1)

def de_queue(queue, elem):
    elem.time = 0
    stack1 = queue.s1
    stack2 = queue.s2
    if not is_empty(stack2):
        elem.x = top(stack2)
        pop(stack2)
        elem.time += 1
        return
    if not is_empty(stack1):
        while not is_empty(stack1):
            x = top(stack1)
            pop(stack1)
            push(stack2, x)
            elem.time += 2
    elem.x = top(stack2)
    pop(stack2)
    elem.time += 1

def destroy_queue(queue):
    destroy_stack(queue.s1)
    destroy_stack(queue.s2)

def main():
    n = int(input())
    queue = Queue()
    init_queue(queue, n)
    elem = DeQElem()
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'I':
            x = int(cmd[1])
            en_queue(queue, x)
        else:
            if is_q_empty(queue):
                print("ERROR")
            else:
                de_queue(queue, elem)
                print(f"{elem.x} {elem.time}")
    destroy_queue(queue)
    del elem

main()