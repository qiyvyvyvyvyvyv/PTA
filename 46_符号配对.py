"""
请编写程序检查C语言源程序中下列符号是否配对：“/*” 与 “*/”、“(” 与 “)”、“[” 与 “]”、“{” 与 “}”。
输入格式：
输入为一个C语言源程序。当读到某一行中只有一个句点“.”和一个回车的时候，
标志着输入结束。程序中需要检查配对的符号不超过100个。
输出格式：
首先，如果所有符号配对正确，则在第一行中输出YES，否则输出NO。
然后在第二行中指出第一个不配对的符号：如果缺少左符号，则输出“?-右符号”；如果缺少右符号，则输出“左符号-?”。
"""
from enum import Enum
import sys

kMaxSize = 100  # 栈的最大容量
# 配对符号类型。依次对应：
# 程序结尾、左注释、右注释、{、}、[、]、(、)、其它符号
class Token(Enum):
    end, lc, rc, lbrc, rbrc, lbrkt, rbrkt, lpr, rpr, others = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

class ErrorCode(Enum):
    # 成功、缺少左符号、缺少右符号
    ok, left_no_match, right_no_match = 0, 1, 2

class ResultNode():  # 符号匹配结果存储结点
    def __init__(self, code):
        self.code = code  # 匹配结果
        self.token = None  # 匹配不成功的符号类型

def getchar():
    # 从输入中读取一个字符
    c = sys.stdin.read(1)
    return c

def GetToken(c):
    # 从输入中读取并返回一个符号类型
    # 外部调用方法：GetToken(getch())
    ret = Token.others
    if c == '{':
        ret = Token.lbrc
    elif c == '[':
        ret = Token.lbrkt
    elif c == '(':
        ret = Token.lpr
    elif c == '}':
        ret = Token.rbrc
    elif c == ']':
        ret = Token.rbrkt
    elif c == ')':
        ret = Token.rpr
    elif c == '/':  # 多读一个符号，判断是否左注释
        c = getchar()
        if c == '*':
            ret = Token.lc
        else:
            ret = GetToken(c)  # 若不是左注释，要判断当前c的类型
    elif c == '*':  # 多读一个符号，判断是否右注释
        c = getchar()
        if c == '/':
            ret = Token.rc
        else:
            ret = GetToken(c)  # 若不是右注释，要判断当前c的类型
    elif c == '\n':  # 判断是否程序末尾
        c = getchar()
        if c == '.':  # 如果回车跟一个句点，则检查后面是否跟一个回车
            c = getchar()
            if c == '\n': ret = Token.end
        # 若不是结尾，则需要判断当前c的类型
        if ret != Token.end: ret = GetToken(c)
    return ret

def PrintSymbol(token):
    # 根据token类型输出符号
    if token == Token.lc:
        print("/*", end="")
    elif token == Token.lbrc:
        print("{", end="")
    elif token == Token.lbrkt:
        print("[", end="")
    elif token == Token.lpr:
        print("(", end="")
    elif token == Token.rc:
        print("*/", end="")
    elif token == Token.rbrc:
        print("}", end="")
    elif token == Token.rbrkt:
        print("]", end="")
    elif token == Token.rpr:
        print(")", end="")

def IsMatched(left, right):
    # 判断左右符号是否在类型中相邻
    return (right.value == (left.value + 1))

class Stack:
    def __init__(self):
        self.kMaxSize = 1000
        self.size = 0
        self.top = -1
        self.data = [0] * kMaxSize

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.size == self.kMaxSize

    def push(self, item):
        if self.isFull():
            print("Stack 满")
            return
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if self.isEmpty():
            print("Stack 空")
            return None
        self.top -= 1
        return self.data[self.top + 1]

def SymbolMatching():
    stack = Stack()
    while True:
        c = getchar()
        token = GetToken(c)
        if token == Token.end:
            break
        elif token == Token.others:
            continue
        else :
            if stack.isFull():
                print("Stack 满")
                break
            elif token == Token.lc:
                stack.push(token)
            elif token == Token.lbrc:
                stack.push(token)
            elif token == Token.lbrkt:
                stack.push(token)
            elif token == Token.lpr:
                stack.push(token)
            elif token == Token.rc :
                if stack.isEmpty():
                    result = ResultNode(ErrorCode.right_no_match)
                    result.token = token
                    return result
                else:
                    left = stack.pop()
                    if not IsMatched(left, token):
                        result = ResultNode(ErrorCode.left_no_match)
                        result.token = left
                        return result
            elif token == Token.rbrc :
                if stack.isEmpty():
                    result = ResultNode(ErrorCode.right_no_match)
                    result.token = token
                    return result
                else:
                    left = stack.pop()
                    if not IsMatched(left, token):
                        result = ResultNode(ErrorCode.left_no_match)
                        result.token = left
                        return result
            elif token == Token.rbrkt :
                if stack.isEmpty():
                    result = ResultNode(ErrorCode.right_no_match)
                    result.token = token
                    return result
                else:
                    left = stack.pop()
                    if not IsMatched(left, token):
                        result = ResultNode(ErrorCode.left_no_match)
                        result.token = left
                        return result
            elif token == Token.rpr :
                if stack.isEmpty():
                    result = ResultNode(ErrorCode.right_no_match)
                    result.token = token
                    return result
                else:
                    left = stack.pop()
                    if not IsMatched(left, token):
                        result = ResultNode(ErrorCode.left_no_match)
                        result.token = left
                        return result
    if stack.isEmpty():
        return ResultNode(ErrorCode.ok)
    else:
        result = ResultNode(ErrorCode.left_no_match)
        result.token = stack.pop()
        return result


"""
# 程序结尾、左注释、右注释、{、}、[、]、(、)、其它符号
class Token(Enum):
    end, lc, rc, lbrc, rbrc, lbrkt, rbrkt, lpr, rpr, others = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
"""
def main():
    result = SymbolMatching()  # 读入程序并执行匹配
    if result.code == ErrorCode.ok:  # 若匹配成功
        print("YES")
    else:  # 若匹配不成功
        print("NO")
        if result.code == ErrorCode.left_no_match:  # 左半符不匹配
            PrintSymbol(result.token)
            print("-?")
        else:  # 右半符不匹配
            print("?-", end="")
            PrintSymbol(result.token)
            print()

main()


