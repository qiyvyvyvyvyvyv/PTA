"""
本题要求实现一个函数，函数接收一个数组list，
以及整数i。若i位置不含于[1,len(list)]，则输出position error 并返回，否则将给定数组list的第i项删除
"""
def Remove(lst, i):
    if i >= 1 and i <= len(lst):
        lst.pop(i-1)
    else:
        print("position error")
    return lst