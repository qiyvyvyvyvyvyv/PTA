"""
伊娃喜欢收集全宇宙的硬币，包括火星币等等。
一天她到了一家宇宙商店，这家商店可以接受任何星球的货币，
但有一个条件，无论什么价格，都必须用2枚硬币一次付清，不能多也不能少。而她有多达10^5个硬币，于是求助于你。
给定任一个价格，请帮她找出可以付款的2枚硬币
第 1 行给出 2 个正整数：n为硬币枚数、m为伊娃要付清的价格；第 2 行给出 n枚硬币的面值，均为不超过 500 的正整数。
同行数字间以空格分隔
在一行中输出两枚硬币的面值v1和v2，以 1个空格分隔，满足条件v1+v2=m ，并且v1≤v2
如果这样的解不唯一，输出v1最小的那个解
如果解不存在，则输出 No Solution
"""
# def main():
#     n, m = map(int, input().split())
#     coin_price = list(map(int, input().split()))
#     i, start, end = 0, 0, 0
#     while i < len(coin_price):
#         price = coin_price[i]
#         last_price = m - price
#         for j in range(n):
#             if coin_price[j] == last_price and i != j:
#                 if start == 0 and end == 0:
#                     start = i
#                     end = coin_price.index(last_price)
#                 elif coin_price[start] > coin_price[i]:
#                     start = i
#                     end = coin_price.index(last_price)
#         i += 1
#     if start == 0 and end == 0:
#         print("No Solution")
#     else:
#         print(coin_price[start], coin_price[end])
def main():
    n, m = map(int, input().split())
    coins = list(map(int, input().split()))

    pos = {}
    for idx in range(n):
        val = coins[idx]
        if val not in pos:
            pos[val] = []
        pos[val].append(idx)

    res = None
    for i in range(n):
        a = coins[i]
        b = m - a
        if b not in pos:
            continue
        # 遍历该面值所有下标
        for j in pos[b]:
            if j != i:  # 核心：不能是同一个硬币
                v1 = min(a, b)
                v2 = max(a, b)
                if res is None or v1 < res[0]:
                    res = (v1, v2)
                break

    if res is None:
        print("No Solution")
    else:
        print(res[0], res[1])


if __name__ == '__main__':
    main()