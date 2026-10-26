"""
KMP算法之求解next数组
"""
kMaxSize = 1001


class StringNode:
    def __init__(self):
        self.data = [''] * kMaxSize
        self.length = 0


def InitStr():
    str = StringNode()
    return str


# 算法4-1：字符串插入操作StrInsert(s, pos, t)
def StrInsert(s, pos, t):
    n = s.length
    m = t.length

    if pos < 1 or pos > n + 1 or (m + n) > kMaxSize:
        print("error")
        return s  # 错误，则不能插入，返回原字符串

    for i in range(n, pos - 1, -1):  # 将子串后移，给t留出空位
        s.data[i + m - 1] = s.data[i - 1]

    for i in range(m):
        s.data[pos - 1 + i] = t.data[i]  # 将t插入s
    s.length = n + m
    return s  # Python参数改变，需要返回


# 算法4-1 结束

# 算法4-2：字符串删除操作StrRemove(s, pos, len)
def StrRemove(s, pos, length):
    n = s.length
    if (pos + length - 1) <= n:  # 从待删除位置到Length后面还有串拷贝到前面
        for i in range(pos + length - 1, n + 1):  # i=n处理结束符
            s.data[i - length] = s.data[i]
        s.length = n - length
    else:  # 需要将从数组下标pos-1开始的所有字符都删掉
        s.length = pos - 1
    return s


def ReadString():
    s = InitStr()  # 初始化StringNode类对象
    data = input()
    for i in range(len(data)):
        s.data[i] = data[i]  # 读入字符串
    s.length = len(data)  # 字符串的长度
    return s


def PrintString(s):
    for i in range(s.length):
        print(s.data[i], end='')


def GetNext(t):
    if t.length == 0:
        return []
    next_list = [0] * t.length
    next_list[0] = -1
    i, j = 1, 0
    while i < t.length:
        while j > 0 and t.data[i] != t.data[j]:
            j = next_list[j - 1] + 1
        if t.data[i] == t.data[j]:
            j += 1
        next_list[i] = j - 1
        i += 1
    return next_list


    # next数组保存的是长度
    # n = t.length
    # next_arr = [-1] * n
    # k = -1  # k 表示当前最长相等前后缀的长度（也是前缀的末位下标）
    # j = 0
    # while j < n - 1:
    #     if k == -1 or t.data[j] == t.data[k]:
    #         k += 1
    #         j += 1
    #         next_arr[j] = k
    #     else:
    #         k = next_arr[k]  # 关键：回退，不是回到 0
    # return next_arr

    # # if t.length == 0:
    #     #     return []
    #     # next_list = [0] * t.length
    #     # next_list[0] = -1
    #     # i, j = 1, -1
    #     # while i < t.length:
    #     #     if j == -1 or t.data[i] == t.data[j]:
    #     #         next_list[i] = j
    #     #         i += 1
    #     #         j += 1
    #     #     else:
    #     #         j = next_list[j]
    #     # return next_list


def main():
    t = ReadString()
    nextArray = GetNext(t)
    print(' '.join(map(str, nextArray)))


main()