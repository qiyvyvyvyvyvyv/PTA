"""
后缀表达式,指的是不包含括号,运算符放在两个运算对象的后面,
所有的计算按运算符出现的顺序,严格从左向右进行(不再考虑运算符的优先规则)。
本题要求使用之前实现的顺序栈类以及本题提供的两个辅助函数来实现一个目标函数，
该函数接收一个后缀表达式，返回该后缀表达式的计算结果。
不考虑后缀表达式不规范或除数为0等出错情况
"""
from enum import Enum

NIL = -1
ErrorCode = 1e9  # 错误代码
kMaxSize = 1000  # 表达式字符串的最大长度为kMaxSize-1

class StackNode:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.data = [None] * capacity

def InitStack(capacity):
    stack = StackNode(capacity)
    return stack


def IsFull(stack):
    return stack.top == stack.capacity - 1


def IsEmpty(stack):
    return stack.top == -1


def Push(stack, x):
    if IsFull(stack):
        print("Stack is full.")
        return
    stack.top += 1
    stack.data[stack.top] = x


def Top(stack):
    if IsEmpty(stack):
        print("Stack is empty.")
        return -1
    return stack.data[stack.top]


def Pop(stack):
    if IsEmpty(stack):
        print("Stack is empty.")
        return
    stack.top -= 1

# 销毁栈
def DestroyStack(stack):
    stack.data = None
    stack.top = -1
    stack.capacity = 0

class TokenType(Enum):  # 定义枚举类
    plus = 1
    minus = 2
    times = 3
    divide = 4
    mod = 5
    operand = 6
    EndCode = 7

# 获取字符串s的第p位置的数据
def GetToken(s, p):  # 获得字符串s的第p位置的数据
    i = p
    ret = None
    num = 0
    while i < len(s) and s[i] == ' ':  # 处理空格
        i += 1
    if i < len(s):
        if s[i] == '+':
            ret = TokenType.plus
            i += 1
        elif s[i] == '-':
            ret = TokenType.minus
            i += 1
        elif s[i] == '*':
            ret = TokenType.times
            i += 1
        elif s[i] == '/':
            ret = TokenType.divide
            i += 1
        elif s[i] == '%':
            ret = TokenType.mod
            i += 1
        elif s[i] == '\0':
            ret = TokenType.EndCode
        else:
            ret = TokenType.operand
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
        p = i
    if ret is None:
        ret = TokenType.operand
    return ret, num, p

# 计算op1 token op2的值
def Calculate(op1, token, op2):
    ret = None
    if token == TokenType.plus:
        ret = op1 + op2
    elif token == TokenType.minus:
        ret = op1 - op2
    elif token == TokenType.times:
        ret = op1 * op2
    elif token == TokenType.divide:
        if op2 == 0:
            print("Error: Division by zero")
            ret = ErrorCode
        else:
            ret = op1 // op2
    elif token == TokenType.mod:
        if op2 == 0:
            print("Error: Modulo by zero")
            ret = ErrorCode
        else:
            ret = op1 % op2
    return ret


# 算法3-13：后缀表达式求值  PostFixEval(expr)  注意：这里仅处理非负操作数
def PostFixEval(expr):  # 后缀表达式expr存储为字符串   类型:str
    list = expr.strip().split(" ")
    stack = InitStack(kMaxSize)
    for i in range(len(list)):
        token, num, p = GetToken(list[i], 0)
        if token == TokenType.operand:
            Push(stack, num)
        else:
            op2 = Top(stack)
            Pop(stack)
            op1 = Top(stack)
            Pop(stack)
            Push(stack, Calculate(op1, token, op2))
    return Top(stack)

if __name__ == '__main__':
    expr = input()
    print(PostFixEval(expr))