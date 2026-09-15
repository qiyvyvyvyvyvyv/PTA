"""
没什么好说的 反转函数reverse() 直接修改原数组 将原数组反转
"""
def ReverseArray1(array):
    array.reverse()
    return array

arr = [1,2,3,4,5,6,7,8]
print(ReverseArray1(arr))