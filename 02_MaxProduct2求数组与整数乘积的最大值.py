"""
这里没什么好说的 调用了python中的函数max找到数组中最大数
乘积返回
"""
def MaxProduct2(array,m):
    max_num = max(array)
    return max_num * m

arr = [1,5,10,6,4,8,7,6]
m = 5
print(MaxProduct2(arr,m))