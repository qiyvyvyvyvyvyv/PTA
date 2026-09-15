"""
本题要求实现一个函数，函数接收一个数组list，
整数i以及整数x。若i位置不含于[1,len(list)+1]，
则输出position error 并返回，否则对给定数组list的第i项前插入值x
"""
def Insert(lst,i,x):
    if i >= 1 and i <= len(lst)+1:
        lst.insert(i-1,x)
    else:
        print("position error")
    return lst
