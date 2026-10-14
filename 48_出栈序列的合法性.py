"""
给定一个最大容量为 m 的堆栈，将 n 个数字按 1, 2, 3, ..., n 的顺序入栈，允许按任何顺序出栈，
则哪些数字序列是不可能得到的？例如给定 m=5、n=7，
则我们有可能得到{ 1, 2, 3, 4, 5, 6, 7 }，但不可能得到{ 3, 2, 1, 7, 5, 6, 4 }
m（堆栈最大容量）、n（入栈元素个数）、k（待检查的出栈序列个数）、sequences（待检查的出栈序列）。
最后 k 行，每行给出 n 个数字的出栈序列。所有同行数字以空格间隔。
对每一行出栈序列，如果其的确是有可能得到的合法序列，就在一行中输出“YES”，否则输出“NO”
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

def is_possible_stack_sequence(m, n, k, sequences: list):
    results = []
    for sequence in sequences:
        stack = Stack(m)
        for i in range(1, n + 1):
            stack.push(i)
            while not stack.isEmpty() and stack.gettop() == sequence[0]:
                stack.pop()
                sequence.pop(0)
            if stack.isFull():
                break
        results.append("YES" if stack.isEmpty() else "NO")
    return results

if __name__ == '__main__':
    m, n, k = map(int, input().split())
    sequences = [list(map(int, input().split())) for _ in range(k)]

    # 输出
    results = is_possible_stack_sequence(m, n, k, sequences)
    for result in results:
        print(result)