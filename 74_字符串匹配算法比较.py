"""
给定两个由英文字母组成的字符串 string 和 pattern，
要求找到 pattern 在 string 中第一次出现的位置，
并将此位置后的 string 的子串输出。如果找不到，则输出“Not Found”
"""
kMaxSize = 1001
class Node:
    def __init__(self):
        self.data=['']*kMaxSize
        self.length=0

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

def PatternMatchKMP(s, t):
    if t.length == 0:
        return t
    if s.length == 0:
        return None
    nextArray = GetNext(t)
    i, j = 0, 0
    while i < s.length and j < t.length:
        if s.data[i] == t.data[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = nextArray[j - 1] + 1
    if j == t.length:
        return i - t.length
    return -1

def PatternMatch(s, t):#待测试的匹配算法放在这个函数里
    s1 = Node()
    t1 = Node()
    s1.data = s
    t1.data = t
    s1.length = len(s)
    t1.length = len(t)
    # 返回t在s中首次出现的位置，位置是数组的下标
    return PatternMatchKMP(s1, t1)

def main():
    s = input()
    n = int(input().strip())
    for _ in range(n):
        pattern = input()
        p = PatternMatch(s, pattern)
        if p != -1:
            print('Find:',s[p:])
        else:
            print("Not Found")

main()