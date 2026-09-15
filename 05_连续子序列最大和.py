"""
函数接收一个已经创建好的列表对象s，
返回给定数组s的最大子序列和、该序列的头坐标和尾坐标
"""
def MaxSubsequenceSum3( s ):
    """
    :param s: 传入列表
    实现思路

    :return:
    """
    start, end, current_num, global_num, i = 0, 0, s[0], s[0], 1
    while i < len(s):
        if current_num + s[i] < 0:
            start = i + 1
            current_num = 0
        else:
            current_num += s[i]
        if current_num < global_num:
            i += 1
            continue
        global_num = current_num
        end = i
        i += 1
    return global_num, start, end

print(MaxSubsequenceSum3( [125,-84,75,61,-54,32,26,-51] ))