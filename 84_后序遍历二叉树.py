"""
给定二叉树类，本题要求实现一个后序遍历二叉树对象的函数
"""


# 算法5-4. 后序遍历二叉树 PostOrder(tree)
class Node:
    def __init__(self, data, left_tree=None, right_tree=None):
        self.data = data
        self.left = left_tree
        self.right = right_tree

def Visit(tree):
    print(tree.data)

def CreateBinaryTree(value, left_tree=None, right_tree=None):
    tree = Node(value, left_tree, right_tree)
    return tree

def PostOrder(tree):
    if tree.left is not None:
        PostOrder(tree.left)
    if tree.right is not None:
        PostOrder(tree.right)
    Visit(tree)

def main():
    data = input()
    left = CreateBinaryTree(data)
    data = input()
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    PostOrder(tree)


main()