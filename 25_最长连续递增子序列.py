"""
给定一个顺序存储的线性表，请设计一个算法查找该线性表中最长的连续递增子序列。
例如，(1,9,2,5,7,3,4,6,8,0)中最长的递增子序列为(3,4,6,8)。
输入格式：
输入第1行给出正整数n（≤10^5）；第2行给出n个整数，其间以空格分隔。
输出格式：
在一行中输出第一次出现的最长连续递增子序列，数字之间用空格分隔，序列结尾不能有多余空格
"""
kMaxSize = 100000
class ListNode:
    def __init__(self):
        self.data = [0] * kMaxSize
        self.last = -1

def ReadInput():
    arrlist = ListNode()
    n = int(input())
    data = list(map(int, input().split()))
    for i in range(n): arrlist.data[i] = data[i]
    arrlist.last = n - 1
    return arrlist

def LongestCIS(arrlist):
    """
    查找线性表中最长的连续递增子序列
    :param arrlist:
    :return: 最长连续递增子序列的起始位置和长度
    时间复杂度：O(n)
    整体思路: 遍历数组 使用到start end max_len以及max_start
    遍历数组时如果当前元素大于前一个元素则end加1
    否则判断end - start + 1是否大于max_len如果是则更新max_len和max_start
    遍历结束后还需要判断一次end - start + 1是否大于max_len
    因为最长的连续递增子序列可能在数组的末尾
    而循环更新max_len和max_start的条件是后面的一个数小于当前元素
    最后返回max_start和max_len
    """
    max_len = 0
    start = 0
    end = 0
    for i in range(1, arrlist.last + 1):
        if arrlist.data[i] > arrlist.data[i - 1]:
            end = i
        else:
            if end - start + 1 > max_len:
                max_len = end - start + 1
                max_start = start
            start = i
    if end - start + 1 > max_len:
        max_len = end - start + 1
        max_start = start
    return max_start, max_len

def PrintResult(arrlist, left, max_len):
    for i in range(left, left+max_len-1):
        print(arrlist.data[i], end=' ')
    print(arrlist.data[left+max_len-1])

arrlist = ReadInput()
left, max_len = LongestCIS(arrlist)
PrintResult(arrlist, left, max_len)