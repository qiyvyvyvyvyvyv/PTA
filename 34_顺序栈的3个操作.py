"""
给出顺序栈类的定义，要求实现三个函数(类方法)，分别实现对自定义顺序栈类的push、top和pop操作。
Push函数接收一个数据x，若栈已满则报错，输出”Stack is full.”，否则函数将x压入栈顶。
Top函数若栈为空则报错，输出”Stack is empty.”，并返回-1，否则返回栈顶数据。
Pop函数若栈为空则报错，输出”Stack is empty.”，否则将原栈顶数据弹出栈
"""
class StackNode:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.data = [None] * capacity

# 初始化
def InitStack(capacity):
    stack = StackNode(capacity)
    return stack

# 判满
def IsFull(stack):
    return stack.top == stack.capacity - 1

# 判空
def IsEmpty(stack):
    return stack.top == -1

# 算法3-1：顺序栈的入栈操作 Push (stack, x)
def Push(stack, x):
    if IsFull(stack):
        print("Stack is full.")
    else:
        stack.data[stack.top + 1] = x
        stack.top += 1
# 算法3-1 结束

# 算法3-2：顺序栈的取顶操作 Top (stack)
def Top(stack):
    if IsEmpty(stack):
        print("Stack is empty.")
        return -1
    else:
        return stack.data[stack.top]
# 算法3-2 结束

# 算法3-3：顺序栈的出栈操作 Pop (stack)
def Pop(stack):
    if IsEmpty(stack):
        print("Stack is empty.")
    else:
        stack.data[stack.top] = None
        stack.top -= 1
# 算法3-3 结束

def DestroyStack(stack):
    del stack

def main():
    n = int(input())
    stack = InitStack(n)
    for i in range(n+1):
        x = int(input())
        Push(stack, x)
    for i in range(n+1):
        print(Top(stack))
        Pop(stack)
    DestroyStack(stack)
main()