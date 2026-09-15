"""
在顺序表list中查找元素x
"""
def Search(lst, x):
    if x in lst:
        return lst.index(x)
    else:
        return -1