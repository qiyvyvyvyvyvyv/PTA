"""
本题要求实现一个能使用Sunday算法将s字符串与t字符串相匹配的函数。
若存在s的子串与t相同则认为匹配成功，返回该子串的头节点；否则认为匹配失败返回None。
"""
def PatternMatchSunday(s, t):
    m, n = len(t), len(s)
    if m == 0:
        return t
    if m > n or n == 0:
        return None
    num = hash(t)
    t_dict = {}
    for i in range(m):
        t_dict[t[i]] = m - i
    start, end = 0, m - 1
    while end < n:
        if hash(s[start:end+1]) == num:
            return start
        else:
            c = s[end + 1]
            if c in t_dict:
                start += t_dict[c]
            else:
                start += m
            end = start + m - 1
    return None

def main():
    s = input()
    t = input()
    p = PatternMatchSunday( s,  t)
    if p == None:
        print('no match!')
    else:
        print('match')
main()