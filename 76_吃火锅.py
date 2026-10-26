"""
微信朋友圈有一张图，上面的文字是：这种天气你有什么破事打电话给我基本没用。但是如果你说“吃火锅”，那就厉害了，我们的故事就开始了。
本题要求你实现一个程序，自动检查你朋友给你发来的信息里有没有“chi1 huo3 guo1”
输入每行给出一句不超过 80 个字符的、以回车结尾的朋友信息，信息为非空字符串，仅包括字母、数字、空格、可见的半角标点符号。
当读到某一行只有一个英文句点“.”时，输入结束，此行不算在朋友信息里
首先在一行中输出朋友信息的总条数。然后对朋友的每一行信息，检查其中是否包含 “chi1 huo3 guo1”，
并且统计这样厉害的信息有多少条。在第二行中首先输出第一次出现 “chi1 huo3 guo1” 的信息是第几条（从 1 开始计数），
然后输出这类信息的总条数，其间以一个空格分隔。题目保证输出的所有数字不超过 100。
如果朋友从头到尾都没提 “chi1 huo3 guo1” 这个关键词，则在第二行输出一个表情 “-_-#”
"""
def getNext(s):
    next_list = [-1] * len(s)
    i, j = 0, -1
    while i < len(s) - 1:
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            next_list[i] = j
        else:
            j = next_list[j]
    return next_list

def KMP(s, t):
    if len(s) < len(t):
        return False
    next_list = getNext(t)
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = next_list[j]
    return j == len(t)

def main():
    s = []
    while True:
        s.append(input())
        if s[-1] == '.':
            break
    the_frist = -1
    count, i = 0, 0
    while True:
        t = s[i]
        if t == '.':
            break
        if KMP(t, 'chi1 huo3 guo1'):
            if the_frist == -1:
                the_frist = i
            count += 1
        i += 1
    print(len(s) - 1)
    if count == 0:
        print("-_-#")
    else:
        print(the_frist + 1, count)

main()