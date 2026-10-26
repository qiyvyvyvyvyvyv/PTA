"""
给定二叉树类，本题要求实现一个中序遍历二叉树对象的函数
"""
# 算法5-3：中序遍历二叉树 InOrder(tree)
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

def InOrder(tree):
    if tree.left != None:
        InOrder(tree.left)
    Visit(tree)
    if tree.right != None:
        InOrder(tree.right)

def main():
    data = input()
    left = CreateBinaryTree(data)
    data = input()
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    InOrder(tree)


main()