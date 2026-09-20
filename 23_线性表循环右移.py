"""
给定顺序表A=(a1,a2,…,an)，请设计一个时间和空间上尽可能高效的算法将该线性表循环右移指定的m位
例如，(1,2,5,7,3,4,6,8)循环右移3位（m=3)后的结果是(4,6,8,1,2,5,7,3)。
输入格式：
第1行输入n (1≤n≤100)、m（m≥0）；
第2行输入n个整数。
输出格式：
输出循环右移m位以后的整数序列
"""
def RightShift(array, n, m):
    m %= n
    list1 = array[n - m:]
    array[n - m:] = array[:n - m]
    array[:n - m] = list1

def main():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    m %= n
    RightShift(array, n, m)
    for i in range(n - 1):
        print(array[i], end=' ')
    print(array[n - 1])

main()