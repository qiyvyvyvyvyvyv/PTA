"""
给定python自带的哈希方法，本题要求实现一个能使用KR算法将s字符串与t字符串相匹配的函数。
若存在s的子串与t相同则认为匹配成功，返回该子串的头节点；否则认为匹配失败返回None
"""
def PatternMatchKR(s, t):
    m, n = len(t), len(s)
    if m == 0:
        return t
    if m > n or n == 0:
        return None
    num = hash(t)
    start, end = 0, m - 1
    while end < n:
        if hash(s[start:end+1]) == num:
            for i in range(m):
                if s[start+i] != t[i]:
                    start += 1
                    end += 1
                    break
            return t
        else:
            start += 1
            end += 1
    return None

def main():
    s = input()
    t = input()
    p = PatternMatchKR( s,  t)
    if p == None:
        print('no match!')
    else:
        print('match')
main()