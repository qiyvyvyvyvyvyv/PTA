"""
给定一个数组和一个整数k，请设计一个线性时间的算法来计算每个长度为k的相邻子数组的最大值。
设长度为k的相邻子数组的左端点为left，则其右端点就是left+k−1，
我们称这个区间[left,left+k−1]为一个观察窗口。
令left从数组下标0开始向右滑动，则观察窗口就相应地向右滑动。
题目要求你输出滑动过程中每个窗口内的最大值。例如，在k = 3时，
数组{1, 2, 3, 1, 4, 5, 2, 3, 6}对应的输出为{3, 3, 4, 5, 5, 5, 6}
"""
def max_sliding_window(nums, k):
    max_num = max(nums[:k])
    start, end = 0, k - 1
    max_index = nums.index(max_num, start, end+1)
    result = [max_num]
    while end != len(nums) - 1:
        # {1, 2, 3, 1, 4, 5, 2, 3, 6}
        #           k
        start += 1
        end += 1
        if max_index < start:
            max_num = max(nums[start:end+1])
            max_index = nums.index(max_num, start, end+1)
        if max_num < nums[end]:
            max_num = nums[end]
            max_index = end
        result.append(max_num)
    return result


if __name__ == '__main__':

    n, k = [int(i) for i in input().split()[:2]]
    nums = [int(i) for i in input().split()]
    # 调用函数并输出结果
    result = max_sliding_window(nums, k)
    for i in result[:-1]:
        print(i, end=" ")
    print(result[-1])