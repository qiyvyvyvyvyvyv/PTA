"""
大整数相加运算(只处理a+b>0的情况)
要求实现一个函数，函数接收两个BigInt类的对象a和b。
函数通过遍历a和b的digits数字数组获得a和b所表示的大整数的和，并
将该和作为一个BigInt对象返回。(只处理a+b>0的情况)
"""
kMaxSize = 1000
ErrorCode = -1
class BigIntNode:
    def __init__(self):
        self.digits = [0] * kMaxSize  # 各位数字从低位到高位顺次存储
        self.length = 0  # 位数
        self.sign = 1  # 正负
    # array = []
    # for i in range(c.length):
    #      array.append(c.digits[i])
    # c.digits = array
def BigIntAdd(a, b):
    """
    大整数相加
    :param a: 第一个大整数
    :param b: 第二个大整数
    :return: 两个大整数的和
    从高位到低位逐位相加/减
    如果出现进位则进位
    如果出现借位则借位
    最后返回结果
    :时间复杂度:O(n)
    当然 注释掉的是旧版思路 不太好
    """
    # 找到较大的数
    # 现根据正负号 再根据两数实际长度 实在不行了只能遍历
    if a.sign > 0 and b.sign < 0:
        max_list, min_list = a, b
    elif b.sign > 0 and a.sign < 0:
        max_list, min_list = b, a
    else:
        if a.length != b.length:
            max_list, min_list = (a, b) if a.length > b.length else (b, a)
        else:
            max_list, min_list = a, b
            for i in range(a.length - 1, -1, -1):  # 从高位到低位逐位比较
                if a.digits[i] != b.digits[i]:
                    if a.digits[i] > b.digits[i]:
                        max_list, min_list = a, b
                    else:
                        max_list, min_list = b, a
                    break
    i = min(a.length - 1, b.length - 1)
    # 从高位到低位逐位相加/减
    while i >= 0:
        # 都是正数
        if a.sign > 0 and b.sign > 0:
            sum = max_list.digits[i] + min_list.digits[i]
            # 合小于10直接加在当前位置上
            if sum < 10:
                max_list.digits[i] = sum
            # 合大于10
            else:
                # 先取模后存入当前位置
                max_list.digits[i] = sum % 10
                # 由于进位只能进1 因此只需要判断被进为是否为9 如果为9那就说明还需要进位 把该节点置为0 进入下一个节点
                # 找到不需要进位节点 如 109999 + 1
                j = 1
                while max_list.digits[i + j] == 9:
                    max_list.digits[i + j] = 0
                    j += 1
                max_list.digits[i + j] += 1
                # 这里在判断是否需要增加最高位
                # 这里判断的是 如 9000 + 1000
                if i == max_list.length - 1:
                    max_list.length += 1
                # 这里判断的是 如果出现了 999 + 1 的情况
                if i + j > max_list.length - 1:
                    max_list.length += 1
        # 一正一负
        else:
            sum = max_list.digits[i] - min_list.digits[i]
            # 合为正
            if sum > 0:
                max_list.digits[i] = sum
            # 合为负
            elif sum < 0:
                # 先10加上sum 并把结果存入当前位置
                max_list.digits[i] = 10 + sum
                # 去遍历上一位可不可以被错位 如10001 - 9
                j = 1
                # 先找到不是0的高位 并减一
                while max_list.digits[i + j] == 0:
                    j += 1
                max_list.digits[i + j] -= 1
                # 去判断如果被错位高位减一后为0 并且错位高位为最高位 则长度-1
                if max_list.digits[i + j] == 0 and max_list.digits[max_list.length - 1] == 0:
                    max_list.length -= 1
                # 将高位后的节点改为9 由于i + j指向被错位 因此需要先-1
                # 1001
                #    9
                #  998
                j -= 1
                while j > 0:
                    max_list.digits[i + j] = 9
                    j -= 1
            # 合为0 且是最高位
            elif i == max_list.length - 1:
                max_list.length -= 1
                max_list.digits[i] = 0
            # 合为0 但不是最高位
            else:
                max_list.digits[i] = 0
        i -= 1
    return max_list
    # c = BigIntNode()
    # i = min(a.length - 1, b.length - 1)
    # max_len = max(a.length, b.length)
    # max_list = a if a.length > b.length else b
    # while i >= 0:
    #     sum = 0
    #     if a.sign > 0 and b.sign > 0:
    #         sum = a.digits[i] + b.digits[i] + c.digits[i]
    #         if sum < 10:
    #             c.digits[i] = sum
    #         else:
    #             c.digits[i] = sum % 10
    #             c.digits[i + 1] = sum // 10
    #             if i == max_len - 1:
    #                 max_len += 1
    #     elif a.sign > 0 and b.sign < 0:
    #         sum = a.digits[i] - b.digits[i] + c.digits[i]
    #         if sum == 0 and i == max_len - 1:
    #             max_len -= 1
    #         if sum < 0:
    #             c.digits[i] = 10 + sum
    #             if max_list.digits[i + 1] == 1:
    #                 max_len -= 1
    #             c.digits[i + 1] -= 1
    #         else:
    #             c.digits[i] = sum
    #     else:
    #         sum = b.digits[i] - a.digits[i] + c.digits[i]
    #         if sum == 0 and i == max_len - 1:
    #             max_len -= 1
    #         if sum < 0:
    #             c.digits[i] = 10 + sum
    #             if max_list.digits[i + 1] == 1:
    #                 max_len -= 1
    #             c.digits[i + 1] -= 1
    #         else:
    #             c.digits[i] = sum
    #     i -= 1
    # if a.length > b.length and (a.length == max_len or max_len > a.length):
    #     i = b.length
    #     while i <= a.length - 1:
    #         sum = c.digits[i] + a.digits[i]
    #         if sum >= 10:
    #             c.digits[i] = sum % 10
    #             c.digits[i + 1] = sum // 10
    #             if i == a.length - 1:
    #                 a.length += 1
    #         else:
    #             c.digits[i] = sum
    #         i += 1
    #     c.length = a.length
    # elif b.length > a.length and (b.length == max_len or max_len > b.length):
    #     i = a.length
    #     while i <= b.length - 1:
    #         sum = c.digits[i] + b.digits[i]
    #         if sum >= 10:
    #             c.digits[i] = sum % 10
    #             c.digits[i + 1] = sum // 10
    #             if i == a.length - 1:
    #                 a.length += 1
    #         else:
    #             c.digits[i] = sum
    #         i += 1
    #     c.length = b.length
    # else:
    #     c.length = max_len
    # return c
    #  999
    #    1

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
    return x

def main():
    a = ReadBigInt()
    b = ReadBigInt()
    c = BigIntAdd(a, b)
    for i in range(c.length - 1, -1, -1):
        print(c.digits[i], end="")
main()



# def BigIntAdd(a, b):
#     c = BigIntNode()
#     a_num = 0
#     b_num = 0
#     while a_num <= a.length - 1 or b_num <= b.length - 1:
#         sum = 0
#         if a.sign > 0 and b.sign > 0:
#             sum = a.digits[a_num] + b.digits[b_num] + c.digits[a_num]
#             if sum < 10:
#                 c.digits[a_num] = sum
#             else:
#                 c.digits[a_num] = sum % 10
#                 c.digits[a_num + 1] = sum // 10
#                 if a_num == a.length - 1:
#                     c.length += 1
#             c.length += 1
#         elif a.sign > 0 and b.sign < 0:
#             sum = a.digits[a_num] - b.digits[b_num] + c.digits[a_num]
#             if sum != 0:
#                 c.length += 1
#             if sum < 0:
#                 c.digits[a_num] = 10 + sum
#                 c.digits[a_num + 1] -= 1
#             else:
#                 c.digits[a_num] = sum
#         else:
#             sum = b.digits[b_num] - a.digits[a_num] + c.digits[a_num]
#             if sum != 0:
#                 c.length += 1
#             if sum < 0:
#                 c.digits[a_num] = 10 + sum
#                 c.digits[a_num + 1] -= 1
#             else:
#                 c.digits[a_num] = sum
#         a_num += 1
#         b_num += 1
#     while a_num < a.length :
#         c.digits[a_num] += a.digits[a_num]
#         a_num += 1
#         c.length += 1
#     while b_num < a.length :
#         c.digits[b_num] += b.digits[b_num]
#         b_num += 1
#         c.length += 1
#     array = []
#     for i in range(c.length):
#          array.append(c.digits[i])
#     c.digits = array
#     return c
