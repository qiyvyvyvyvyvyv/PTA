"""
你在一家软件公司负责开发新一代智能文档编辑器。产品经理提出了一个特殊需求：重复以下操作删除所有数字字符：
删除第一个数字字符以及它左边最近的非数字字符。
请你返回删除所有数字字符以后剩下的字符串。
注意，该操作不能对左侧没有任何非数字字符的数字执行。
比如用户输入"1hello1"时，系统会自动变成"1hell"
"""
class Stack:
    def __init__(self):
        self.front = 0
        self.Maxsize = 1000
        self.data = [0] * self.Maxsize
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.Maxsize

    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.front -= 1
            self.size -= 1
            num = self.data[self.front]
            self.data[self.front] = 0
            return num

    def push(self, num):
        if self.isFull():
            return None
        else:
            self.data[self.front] = num
            self.front += 1
            self.size += 1


def main():
    s = input()
    stack = Stack()
    for char in s:
        if not char.isdigit():
            stack.push(char)
        else:
            if not stack.isEmpty():
                stack.pop()
            else:
                stack.push(char)
    p = ""
    while not stack.isEmpty():
        p += stack.pop()
    print(p[::-1])

if __name__ == "__main__":
    main()