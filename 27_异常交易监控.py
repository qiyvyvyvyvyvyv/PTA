"""
在金融交易监控系统中，需要检测可能存在的拆分交易（将大额交易拆分为多笔小额交易以规避监管）。
给定一组交易金额列表 transactions（2≤len(transactions)≤10^4，1≤transactions[i]≤10^6，单位：元）
和监管阈值 threshold（1≤threshold≤2×10^6，单位：元），请在交易列表中找到两笔不同的交易，
使得它们的金额之和恰好等于 threshold。返回这两笔交易在列表中的原始索引（即交易发生的顺序位置）。
注意：
每笔交易只能使用一次，不能重复匹配同一笔交易。
若存在多组符合条件的交易对，返回索引较小的交易出现最早的那一组，即优先选择第一笔交易索引最小的组合。
交易金额均为正数
"""
def main():
    in_list = list(map(int, input().split()))
    threshold = int(input())
    for i in range(len(in_list)):
        for j in range(i + 1, len(in_list)):
            if in_list[i] + in_list[j] == threshold:
                print(i, j)
                return
    print("")

if __name__ == "__main__":
    main()