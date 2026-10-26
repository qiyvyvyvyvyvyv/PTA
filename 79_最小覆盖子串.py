"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。s 和 t 由英文字母组成，且字符串长度在[1,10^5]。
注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案
"""
def main():
    s = input()
    t = input()
    n, m = len(s), len(t)
    if m == 0 or n < m:
        print("")
        return

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    missing = m  # 还缺多少个字符
    left = 0  # 窗口左端，只右移
    best_l, best_r = 0, n + 1  # 当前最优窗口
    get = need.get

    for right in range(n):
        ch = s[right]
        c = get(ch, 0)
        if c > 0:  # 命中了"还缺的"字符
            missing -= 1
        need[ch] = c - 1  # 负数 = 窗口里多余

        if missing == 0:  # 已覆盖 t
            while need[s[left]] < 0:  # 左端多余的字符可以丢
                need[s[left]] += 1
                left += 1
            if right + 1 - left < best_r - best_l:
                best_l, best_r = left, right + 1
                if best_r - best_l == m:  # 长度下界，已不可能更短
                    break

    if best_r > n:
        print("")
    else:
        print(s[best_l:best_r])

main()