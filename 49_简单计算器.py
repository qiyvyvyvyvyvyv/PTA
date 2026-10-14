"""
本题要求你为初学数据结构的小伙伴设计一款简单的利用堆栈执行的计算器。
如上图所示，计算器由两个堆栈组成，
一个堆栈 s1存放数字，另一个堆栈 s2存放运算符。
计算器的最下方有一个等号键，每次按下这个键，计算器就执行以下操作：
从 s1 中弹出两个数字，顺序为 n1和 n2
从 s2中弹出一个运算符 op；
执行计算 n2op n1
将得到的结果压回 s1。
直到两个堆栈都为空时，计算结束，最后的结果将显示在屏幕上
n (int): 表达式中数字的个数 numbers (list):
包含 n 个整数的列表，表示表达式中的数字 operators (list): 包含 n-1 个运算符的列表，表示表达式中的运算符。
实现要求：
将输入的数字和运算符按给定顺序分别压入堆栈 s1和 s2 ，
将执行计算的最后结果输出。注意所有的计算都只取结果的整数部分。题目保证计算的中间和最后结果的绝对值都不超过 10^9
如果执行除法时出现分母为零的非法操作，
则在一行中输出：”ERROR: X/0”，其中 X 是当时的分子，然后结束程序
（可以使用exit()函数直接结束程序，不再返回main()函数中执行print()）
"""
class Stack:
    def __init__(self, kMaxSize):
        self.kMaxSize = kMaxSize
        self.size = 0
        self.top = -1
        self.data = [0] * self.kMaxSize

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.size == self.kMaxSize

    def push(self, item):
        if self.isFull():
            print("Stack 满")
            return
        self.top += 1
        self.size += 1
        self.data[self.top] = item

    def pop(self):
        if self.isEmpty():
            print("Stack 空")
            return None
        self.top -= 1
        self.size -= 1
        return self.data[self.top + 1]

    def gettop(self):
        return self.data[self.top]

def simple_calculator(n, numbers, operators):
    stack1 = Stack(n)
    stack2 = Stack(n)
    for number in numbers:
        stack1.push(number)
    for operator in operators:
        stack2.push(operator)
    while not stack1.isEmpty() and not stack2.isEmpty():
        n1 = stack1.pop()
        n2 = stack1.pop()
        op = stack2.pop()
        if op == '+':
            stack1.push(n1 + n2)
        elif op == '-':
            stack1.push(n2 - n1)
        elif op == '*':
            stack1.push(n1 * n2)
        elif op == '/':
            if n1 == 0:
                print(f"ERROR: {n2}/0")
                exit()
            stack1.push(int(n2 / n1))
    return stack1.pop()

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    operators = input().split()

    # 输出
    result = simple_calculator(n, numbers, operators)
    print(result)