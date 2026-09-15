"""
给定存储了n个从大到小排好序的整数，试将任一给定整数x插入数组中合适的位置，以保持结果依然有序
具体来说，不妨假设整数有序序列存储为一个列表array。Python的列表是可以动态伸缩的，
因此插入操作不用考虑最大空间问题。但如果待插入的元素x已经在data中，则不要重复插入，返回False；如果插入成功，则返回True
"""
def DecrSeqInsert( array, x ):
    if x not in array:
        for i in range(len(array)):
            if array[i] <= x:
                array.insert(i, x)
                return True
        if x not in array:
            array.append(x)
            return True
    else:
        return False

DecrSeqInsert([35, 12, 8, 7, 3],10)