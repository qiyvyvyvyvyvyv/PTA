"""
对正整数n和正整数m进行计算，
对1~n与1~m每一项相互乘积求和并返回该和。
例如对于参数n=2，m=3，1∗(1+2+3)+2∗(1+2+3)=18，函数返回值为18
"""
def SumProducts( n , m ):
    if n == 1:
        return 1 * (m * (m + 1) // 2)
    else:
        return n * (m * (m + 1) // 2) + SumProducts(n - 1, m)

sumProducts = SumProducts(2, 3)
print(sumProducts)