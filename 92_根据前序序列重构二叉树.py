"""
给定二叉树类，本题要求实现一个能根据前序序列重构二叉树的函数。(序列中#表空节点)
"""
k = -1  # 当前待处理的元素在preorder中的下标，初始化为-1
class Node:
    def __init__(self, data, left_tree=None, right_tree=None):
        self.data = data
        self.left = left_tree
        self.right = right_tree

def Visit(tree):
    print(tree.data, end=" ")

def CreateBinaryTree(value, left_tree=None, right_tree=None):
    tree = Node(value, left_tree, right_tree)
    return tree

def PostOrder(root):
    if root != None:
        PostOrder(root.left)
        PostOrder(root.right)
        Visit(root)

def PreOrderDeSerialize(preorder, n):
    global k
    preorder = preorder.split() if any(ch.isspace() for ch in preorder) else list(preorder)

    if n <= 0:
        return None
    k += 1

    if k >= n:
        return None

    if preorder[k] == "#":
        return None

    tree = CreateBinaryTree(preorder[k])
    tree.left = PreOrderDeSerialize(preorder, n)
    tree.right = PreOrderDeSerialize(preorder, n)


    return tree


def main():
    # preorder = 'abc##de###f#g##'
    # '1 2 # 4 # # 3 5 # # # '
    # 'abc##de###f#g##'
    preorder = input()
    tree = PreOrderDeSerialize(preorder, len(preorder));
    PostOrder(tree)


main()