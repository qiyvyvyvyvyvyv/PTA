"""
假设以S和X分别表示入栈和出栈操作。如果根据一个仅由S和X构成的序列，
对一个空堆栈进行操作，相应操作均可行（如没有出现删除时栈空）且最后状态也是栈空，
则称该序列是合法的堆栈操作序列。请编写程序，输入S和X序列，判断该序列是否合法。
输入格式：
第1行给出两个正整数n和m，其中n是待测序列的个数，m（≤50）是堆栈的最大容量。
随后n行，每行中给出一个仅由S和X构成的序列。序列保证不为空，且长度不超过100。
输出格式：
对每个序列，如果该序列是合法的堆栈操作序列，在一行中输出YES，否则输出NO
"""
class Stack:
    def __init__(self, size):
        self.capacity = size
        self.top = -1
        self.data = [0] * size

def init_stack(stack, size):
    stack.capacity = size
    stack.top = -1
    stack.data = [0] * size

def is_full(stack):
    return stack.top + 1 == stack.capacity

def is_empty(stack):
    return stack.top == -1

def push(stack, x):
    if is_full(stack):
        return False
    stack.top += 1
    stack.data[stack.top] = x
    return True

def pop(stack):
    if is_empty(stack):
        return False
    stack.top -= 1
    return True

def clear(stack):
    while not is_empty(stack):
        pop(stack)

def destroy_stack(stack):
    del stack

def is_valid_stack_sequence(sequence, max_capacity):
    stack = Stack(max_capacity)
    for char in sequence:
        if char == 'S':
            push(stack, 1)
        elif char == 'X':
            if is_empty(stack):
                return False
            pop(stack)
    return is_empty(stack)

def main():
    n, m = map(int, input().split())
    for _ in range(n):
        sequence = input().strip()
        result = is_valid_stack_sequence(sequence, m)
        print("YES" if result else "NO")

main()