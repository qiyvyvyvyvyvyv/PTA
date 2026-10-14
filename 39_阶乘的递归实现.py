"""
要求使用递归的方法实现一个函数，
该函数接收一个整数n，返回n的阶乘的计算结果
"""
# 算法3-14：阶乘的递归实现 Factorial(n)
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)
# 算法3-14 结束

if __name__ == '__main__':
    n = int(input())
    print(Factorial(n))