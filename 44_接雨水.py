"""
现有n个宽度为1的柱子，给出n个非负整数依次表示柱子的高度，排列后如下图所示，
此时均匀从上空向下撒雨水，计算按此排列的柱子能接住多少雨水。
例如，当输入数组为height=[0,1,0,2,1,0,1,3,2,1,2,1]，该数组的接雨水能力如下图示例，总共可接6个单位
"""
def trap(height):
    # if not height:
    #     return 0
    # n = len(height)
    # left_max = [0] * n
    # right_max = [0] * n
    # left_max[0] = height[0]
    # for i in range(1, n):
    #     left_max[i] = max(left_max[i-1], height[i])
    # right_max[n-1] = height[n-1]
    # for i in range(n-2, -1, -1):
    #     right_max[i] = max(right_max[i+1], height[i])
    # water_trapped = 0
    # for i in range(n):
    #     water_trapped += min(left_max[i], right_max[i]) - height[i]
    # return water_trapped
    """
    核心思路就是 双指针
    我们会记录指针遍历到的左边和右边值最高的柱子
    当遍历到某一个位置时 由于left_max和right_max存储的是最高值 那么旧一定可以保证在遍历过的位置都比left_max和right_max小或相同
    那么当前位置能接的雨水量就取决于较短的柱子 减去当前柱子的高度
    就可以得到接雨水的量
    替代最大值的条件是比left_max和right_max里存储的值更大 那么他其实同时隐含了一个条件就是比之前遍历过的所有位置的柱子都高
    那么就可以保证之前遍历过的柱子一定都比当前柱子矮 也就保证一定可以存储那些水量
    那么为什么一边比另一边小的时候就移动小的一边的指针呢？
    因为存水量是矮的柱子决定的
    """
    left_max, right_max = 0, 0
    left, right = 0, len(height) - 1
    water_trapped = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] > left_max:
                left_max = height[left]
            water_trapped += left_max - height[left]
            left += 1
        elif height[left] >= height[right]:
            if height[right] > right_max:
                right_max = height[right]
            water_trapped += right_max - height[right]
            right -= 1
    return water_trapped

def main():
    height_list = [int(x) for x in input().split()]
    # 4 2 0 3 2 5
    # 0 1 0 2 1 0 1 3 2 1 2 1
    print(trap(height_list))

if __name__ == "__main__":
    main()