"""
给出链式栈类和链式栈节点类的定义，要求实现三个函数(类方法)，分别实现对自定义链式栈类的push、top和pop操作。
Push函数接收一个数据x，函数将x压入栈顶。
Top函数若栈为空则报错，输出”Stack is empty.”，并返回-1，否则返回栈顶数据。
Pop函数若栈为空则报错，输出”Stack is empty.”，否则将原栈顶数据弹出栈
"""
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackHeadNode:
    def __init__(self):
        self.size = 0
        self.top = None

def InitStack():
    stack = StackHeadNode()
    return stack

def IsEmpty(stack):
    return stack.top is None

# 算法3-4：链式栈的入栈操作 Push (stack, x)
def Push(self, x):
    node = StackNode(x)
    node.next = self.top
    self.top = node
    self.size += 1

# 算法3-4 结束

# 算法3-5：链式栈的取顶操作
def Top(self):
    if IsEmpty(self):
        print("Stack is empty.")
        return -1
    else:
        return self.top.data
    pass

# 算法3-5 结束

# 算法3-6：链式栈的出栈操作 Pop (stack)
def Pop(self):
    if IsEmpty(self):
        print("Stack is empty.")
    else:
        self.top = self.top.next
        self.size -= 1

# 算法3-6 结束

def DestroyStack(stack):
    stack.top = None
    stack.size = 0

def main():
    n = int(input())
    stack = InitStack()
    for i in range(n):
        x = int(input())
        Push(stack, x)
    for i in range(n + 1):
        print(Top(stack))
        Pop(stack)
    DestroyStack(stack)

main()