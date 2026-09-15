"""
爆气球对孩子们来说是很好玩的游戏。
假设有 n 只气球被布置在一条直线上，游戏的目标很简单，就是爆掉尽可能多的气球。
但是这里我们加一条特殊的规则 —— 你只能跳一次。我们假设聪明的娃穿了件浑身带刺的衣服，
跳到某个位置，躺平，这样气球只要碰到娃身体的任何部分都会立刻爆炸。那么你的任务就是告诉娃应该跳到哪里，
才能一次爆掉最多的气球。
输入各式
在一行中输出孩子跳跃的位置坐标，使得孩子跳到这个位置然后躺平能够爆掉身下最多的气球；
随后输出能爆掉的气球的最大数量。
如果这个坐标不唯一，输出最小的那个值。
一行中的数字间应有 1 个空格，行首尾不得有多余空格
"""
def max_burst_location(n, h, balloons):
    balloons.sort()
    i, j, max_location = 0, 0, 0
    max_burst = 0
    for i in range(n):
        while j < n and balloons[i] + h >= balloons[j]:
            j += 1
        num = j - i
        if num > max_burst:
            max_burst = num
            max_location = i
    return balloons[max_location], max_burst

print(max_burst_location(11, 120,[-120, -40, 0, 80, 120, 140, 160, 220, 240, 260, 300]))