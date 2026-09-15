"""
使用循环算法对给定的正整数n按序输出1~n的序列。
例如对于参数n=4，函数输出1 2 3 4
"""
def IterativePrint ( n ):
    for i in range(n):
        print(i + 1, end=" ")

IterativePrint(4)