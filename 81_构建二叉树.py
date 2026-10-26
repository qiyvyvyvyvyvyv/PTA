"""
本题要求实现二叉树对象的初始化方法
"""
# 算法5-1：构造二叉树 CreateBinaryTree(value, left_tree, right_tree )
class BinaryTreeNode:
    def __init__(self, data, left_tree=None, right_tree=None):
        self.data = data
        self.left = left_tree
        self.right = right_tree

def CreateBinaryTree(value, left_tree=None, right_tree=None ):
    tree = BinaryTreeNode(value,left_tree,right_tree)
    return tree

def main():
    data = input()
    left = CreateBinaryTree(data)
    data = input()
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    print(tree.data, tree.left.data, tree.right.data)


main()