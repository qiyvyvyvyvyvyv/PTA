"""
给定树类，本题要求实现一个能查找树中带有指定数据的节点的函数
"""
class TreeNode:
    def __init__(self, data, first_child=None, next_sibling=None):
        self.data = data
        self.first_child = first_child
        self.next_sibling = next_sibling

def Search(tree, x):
    if tree == None:
        return None
    if tree.data == x:
        return tree
    else:
        p = Search(tree.first_child, x)
        if p != None:
            return p
        else:
            return Search(tree.next_sibling, x)

def NewTreeNode():
    data = input()
    node_ptr = TreeNode(data)
    return node_ptr

def main():
    tree = NewTreeNode()
    child = NewTreeNode()
    sibling = NewTreeNode()
    tree.first_child = child
    child.next_sibling = sibling
    sibling.next_sibling = NewTreeNode()
    x = input()
    p = Search(tree, x)
    if p != None:
        print(p.data, " is found.")
    else:
        print(x, " is NOT found.")

main()