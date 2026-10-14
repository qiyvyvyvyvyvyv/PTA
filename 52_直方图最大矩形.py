"""
你是一名城市规划师，正在为新开发区设计建筑群。由于地形限制和建筑规范要求，每块地皮上建筑物的最大允许高度已经确定。
现在需要在这些地块中选择连续的区域建造一
座大型综合体建筑（如购物中心、会展中心等），要求建筑必须是矩形且高度不能超过所选区域内任何地块的高度限制。
作为规划师，你需要找出能够建造的最大矩形建筑面积，以最大化土地利用效率和经济效益。
给定一排连续地块的建筑高度限制数组heights，其中每个元素表示对应地块上建筑物的最大允许高度，
每块地的宽度均为标准单位1。请找出在这些地块中能够建造的最大矩形建筑面积。
例如：当地块高度限制为heights=[2,1,5,6,2,3],[5,4,3,2,1]时，最优方案是选择第3、4块地（高度限制为5、6），
建造高度为5、面积为10的矩形建筑
"""
def main():
    heights = list(map(int, input().split()))
    stack = []
    index_list = []
    max_area = 0
    length = len(heights)
    j = -1
    for i in range(length):
        if not stack or heights[i] >= stack[j]:
            stack.append(heights[i])
            index_list.append(i)
            j += 1
        else:
            while stack and heights[i] < stack[j]:
                area = stack.pop() * (i - (index_list[j - 1] if stack else -1) - 1)
                max_area = max(max_area, area)
                j -= 1
                index_list.pop()
            stack.append(heights[i])
            index_list.append(i)
            j += 1

    for k in range(j, -1, -1):
        area = stack.pop() * (length - (index_list[k - 1] if stack else -1) - 1)
        max_area = max(max_area, area)

    print(max_area)
    # 贪心过不了
    # heights = list(map(int, input().split()))
    # length = len(heights)
    # max_area = length
    # max_index = 0
    # max_wide = length
    # wide = 0
    # index = 0
    # area = max_area
    # height = 1
    # for i in range(0, length):
    #     wide += 1
    #     height = min(height, heights[i])
    #     if height == 1:
    #         if heights[i] > height * wide:
    #             wide = 1
    #             height = heights[i]
    #             index = i
    #     if area < height * wide:
    #         area = height * wide
    #         if area > max_area:
    #             max_area = area
    #             max_index = index
    #             max_wide = wide
    #     else:
    #         wide = 1
    #         height = heights[i]
    #         index = i
    # print(max_area)

if __name__ == "__main__":
    main()