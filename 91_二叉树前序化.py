"""
给定二叉树类，本题要求实现将二叉树前序序列化的函数。(输出特殊符号’#’代表空节点)
"""
class Node:
    def __init__(self, data, left_tree=None, right_tree=None):
        self.data = data
        self.left = left_tree
        self.right = right_tree

def CreateBinaryTree(value, left_tree=None, right_tree=None):
    tree = Node(value, left_tree, right_tree)
    return tree

def PreOrderSerialize(tree):
    if tree is None:
        print("#", end=' ')
    else:
        print(tree.data, end=' ')
        PreOrderSerialize(tree.left)
        PreOrderSerialize(tree.right)

def main():
    data = input()
    left = CreateBinaryTree(data)
    data = input()
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    PreOrderSerialize(tree)


main()