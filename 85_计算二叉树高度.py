"""
给定二叉树类，本题要求实现一个返回二叉树高度的函数
"""
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

def Height(tree):
    if tree is None:
        return 0
    else:
        return max(Height(tree.left), Height(tree.right)) + 1

def main():
    data = input()
    left = CreateBinaryTree(data)
    data = input()
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    print(Height(tree))


main()