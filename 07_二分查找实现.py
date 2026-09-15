"""
给定n个从小到大排好序的整数序列data，
以及某待查找整数x，
我们的目标是找到x在data中的位置。
具体来说，不妨假设整数序列存储为一个序列array，这个序列的采用列表list存储。
若有array[i]=x，则返回i；否则返回失败标记None表示没有找到。
二分法是先找到序列的中点array[middle]，
与x进行比较，若array[middle]>x，
则在左边的子序列中查找x；若array[middle]<x，
则在右边的子序列中查找x; 否则两者相等，则
返回中点下标middle
"""
# def BinarySearch( array, x ):
#     length = len(array)
#     i = length // 2
#     if length % 2 == 0:
#         if length == 2:
#             if array[i] == x:
#                 return i
#             if array[i - 1] == x:
#                 return i - 1
#             else:
#                 return None
#         elif x == array[i]:
#             return i
#         elif x == array[i - 1]:
#             return i - 1
#         elif x < array[i - 1]:
#             return BinarySearch(array[:i - 1], x)
#         elif x > array[i]:
#             return BinarySearch(array[i + 1:], x)
#     else:
#         if length == 1:
#             if array[i] == x:
#                 return i
#             else:
#                 return None
#         elif x == array[i]:
#             return i
#         elif x < array[i]:
#             return BinarySearch(array[:i], x)
#         else:
#             return BinarySearch(array[i + 1:], x)
def BinarySearch( array, x ):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (right + left) // 2
        if array[middle] == x:
            return middle
        elif array[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
    return None


print(BinarySearch( [12, 31, 55, 89], 89))