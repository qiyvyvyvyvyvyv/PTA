"""
试在一个长度为n的数组中实现两个栈，
使得二者在元素的总数目为n之前都不溢出，
并保证Push和TopPop操作的时间代价为O(1)
InitStack函数是用n初始化栈2个顺序stack的总容量capacity，并
初始化两个栈顶指针的初值分别是-1和n。
Push 和TopPop 函数中的tag是栈的编号，为1时表示对top1所指的栈顶进行操作，为
2时表示对top2所指的栈顶进行操作
Push函数将x插入第tag个栈。注意：如果第tag个栈已满，
Push函数必须输出“Stack Full”并且返回false。成功插入则返回true。
TopPop函数是标准栈函数Top和Pop的组合，
需要将第tag个栈的栈顶元素从该栈中移除，并返回其值。如果第tag个栈是空的，
则Pop函数必须输出“Stack tag Empty”（其中tag是该栈的编号），并且返回ERROR
"""
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top1 = -1
        self.top2 = capacity
        self.data = [None] * (capacity)

def InitStack(stack, n):
    stack.top1 = -1
    stack.top2 = n
    stack.capacity = n
    stack.data = [None] * (n)

def Push (stack, x, tag):
    if tag == 1:
        if stack.top1 + 1 < stack.top2:
            stack.top1 += 1
            stack.data[stack.top1] = x
            return True
        else:
            print("Stack Full")
            return False
    elif tag == 2:
        if stack.top2 - 1 > stack.top1:
            stack.top2 -= 1
            stack.data[stack.top2] = x
            return True
        else:
            print("Stack Full")
            return False

def Pop (stack, tag):
    if tag == 1:
        if stack.top1 >= 0:
            x = stack.data[stack.top1]
            stack.top1 -= 1
            return x
        else:
            print(f"Stack {tag} Empty")
            return None
    elif tag == 2:
        if stack.top2 < stack.capacity:
            x = stack.data[stack.top2]
            stack.top2 += 1
            return x
        else:
            print(f"Stack {tag} Empty")
            return None

def TopPop(stack, param):
    return Pop(stack, param)


if __name__ == '__main__':
    n = int(input())
    stack = Stack(n)
    InitStack(stack, n)

    commands = []
    while True:
        command = input().split()
        if command[0] == "End":
            break
        commands.append(command)

    for command in commands:
        if command[0] == "Push":
            tag = int(command[1])
            x = int(command[2])
            result = Push(stack, x, tag)
        elif command[0] == "Pop":
            tag = int(command[1])
            result = TopPop(stack, tag)

    # 弹出两个栈的剩余元素
    print("Pop from Stack 1: ", end="")
    while stack.top1 >= 0:
        print(TopPop(stack, 1), end=" ")
    print()
    print("Pop from Stack 2: ", end="")
    while stack.top2 < stack.capacity:
        print(TopPop(stack, 2), end=" ")
