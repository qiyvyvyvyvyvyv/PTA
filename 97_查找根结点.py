"""
给定树类，本题要求实现一个能根据传入的树和当前位置找到根结点的位置的函数
"""
class TreeNode:
    def __init__(self, data, parent=-1):  # 双亲是-1，表示是根
        self.data = data
        self.parent = parent

def FindRoot(tree, x):
    while tree[x].parent != -1:
        x = tree[x].parent
    return x

def main():
    n = int(input())
    tree = []
    for i in range(n):# 读入n个结点的数据和双亲位置
        d,p = input().split()
        tree.append(TreeNode(d,int(p))) #p是父亲索引
    x = int(input())
    root = FindRoot(tree, x)
    print(root,tree[root].data)

main()