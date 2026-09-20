"""
大整数相乘运算
要求实现一个函数，函数接收两个BigInt类的对象a和b。
函数通过遍历a和b的digits数字数组获得a和b所表示的大整数的积，并将该积作为一个BigInt对象返回
"""
kMaxSize = 1000
ErrorCode = -1
class BigIntNode:
    def __init__(self):
        self.digits = [0] * kMaxSize  # 各位数字从低位到高位顺次存储
        self.length = 0  # 位数
        self.sign = 1  # 正负

def BigIntMultiply(a, b):
    # 10000
    #   *
    # 9
    # 123456 * 99
    # 9/18/27/36/45/54
    """
    首先确定结果的位数 a.length + b.length - 1
    开辟结果的数组空间
    从较小的数的高位开始 逐个相乘 结果存入的位置就是 a乘数的位序 + b乘数的位序 然后 +=
    最后处理进位
    从结果数组的低位开始 向高位遍历 处理进位
    :param a: a大整数
    :param b: b大整数
    :return: 大整数乘积
    """
    if a.length == 0 or b.length == 0:
        c = BigIntNode()
        c.length = 1
        return c
    c = BigIntNode()
    c.length = a.length + b.length - 1
    c.digits = [0] * c.length
    i = a.length - 1
    while i >= 0:
        j = b.length - 1
        while j >= 0:
            c.digits[i + j] += a.digits[i] * b.digits[j]
            j -= 1
        i -= 1
    for i in range(c.length):
        if c.digits[i] < 10:
            continue
        elif c.digits[i] >= 10 and i == c.length - 1:
            c.digits.append(0)
            c.length += 1
            j = i + 1
            c.digits[j] += c.digits[i] // 10
            c.digits[i] %= 10
            while c.digits[j] >= 10:
                c.digits.append(0)
                c.length += 1
                c.digits[j + 1] += c.digits[j] // 10
                c.digits[j] %= 10
                j += 1
        elif c.digits[i] >= 10:
            nxt = c.digits[i + 1] + c.digits[i] // 10
            c.digits[i] %= 10
            c.digits[i + 1] = nxt
    if a.sign == 1 and b.sign == 1:
        c.sign = 1
    elif a.sign == -1 and b.sign == -1:
        c.sign = 1
    else:
        c.sign = -1
    return c

def ReadBigInt():
    s = input()
    x = BigIntNode()
    n = len(s)
    i = 0
    if s[0] == '-':
        x.sign = -1
        x.length = n - 1
        i += 1
    else:
        x.sign = 1
        x.length = n
    if x.length > kMaxSize:
        print("error:exceeding the limit of digits")
        x.length = ErrorCode
    else:
        j = x.length - 1
        for char in s[i:]:
            x.digits[j] = int(char)
            i += 1
            j -= 1
        if x.digits[x.length-1] == 0:
            x.length = 0 # 0做特殊处理
    return x
def main():
    a = ReadBigInt()
    b = ReadBigInt()
    c = BigIntMultiply(a, b)
    if c.sign == -1:
        print('-',end='') #打印负号
    for i in range(c.length - 1, -1, -1):
        print(c.digits[i], end="")
main()