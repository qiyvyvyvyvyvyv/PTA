"""
给定两个由英文字母组成的字符串 string 和 pattern，
要求找到 pattern 在 string 中第一次出现的位置，
并将此位置后的 string 的子串输出。如果找不到，则输出“Not Found”
"""
def PatternMatch(s, t):#待测试的匹配算法放在这个函数里
    # 返回t在s中首次出现的位置，位置是数组的下标
    pass

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