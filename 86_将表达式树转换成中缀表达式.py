"""
给定二叉树类，本题要求实现一个将表达式树转换成中缀表达式的函数
"""
class ExprTreeNode:
    def __init__(self, data, left_tree=None, right_tree=None):
        self.data = data
        self.left = left_tree
        self.right = right_tree

def CreateBinaryTree(value, left_tree=None, right_tree=None):
    tree = ExprTreeNode(value, left_tree, right_tree)
    return tree

def PrintInfixExpression(tree):
    if tree is not None:
        print(f"( {tree.left.data} ) {tree.data} ( {tree.right.data} ) ")

def main():
    data = float(input())
    left = CreateBinaryTree(data)
    data = float(input())
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    PrintInfixExpression(tree)

main()