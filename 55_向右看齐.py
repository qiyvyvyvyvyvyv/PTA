"""
N(1≤N≤10^5)头奶牛站成一排，奶牛i的身高为Hi,(1≤Hi≤10^6)。
现在，每头奶牛都在向右看齐。对于奶牛i，如果奶牛j满足i<j，
且Hi<Hj我们说奶牛i仰望奶牛j。求出每头奶牛距离它最近的仰望对象
"""
class Stack:
    def __init__(self, KMaxSize):
        self.KMaxSize = KMaxSize
        self.size = 0
        self.top = -1
        self.data = [0] * self.KMaxSize

    def isFull(self):
        return self.size == self.KMaxSize

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.data[self.top] = 0
            self.top -= 1
            self.size -= 1

    def getTop(self):
        if self.isEmpty():
            return None
        else:
            return self.data[self.top]

    def push(self, item):
        if self.isFull():
            return None
        else:
            self.top += 1
            self.data[self.top] = item
            self.size += 1

def main():
    n = int(input())
    cows = [int(x) for x in input().split()]
    stack = Stack(n)
    index_list = [0] * n
    for i in range(n):
        while not stack.isEmpty() and cows[i] > cows[stack.getTop()]:
            # 6
            # 3 2 6 1 1 2
            # print(i + 1)
            index_list[stack.getTop()] = i + 1
            stack.pop()
        stack.push(i)
    while not stack.isEmpty():
        index_list[stack.getTop()] = 0
        stack.pop()
    for i in range(n):
        print(index_list[i])

main()