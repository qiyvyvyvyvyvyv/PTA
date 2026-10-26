"""
给定树类，本题要求实现一个后序遍历树输出其结点的值的函数
"""
class TreeNode:
    def __init__(self, data, first_child=None, next_sibling=None):
        self.data = data
        self.first_child = first_child
        self.next_sibling = next_sibling

def Search(tree, x):
    node_ptr = tree
    if node_ptr != None:  # 在子孙结点中查找
        if node_ptr.data != x:
            node_ptr = Search(tree.first_child, x)
            if node_ptr == None:  # 不在子孙结点中
                # 在兄弟结点及其子孙中找
                node_ptr = Search(tree.next_sibling, x)
    return node_ptr

def NewTreeNode():
    data = input()
    node_ptr = TreeNode(data)
    return node_ptr

def Visit(tree):
    print(tree.data)

def PostOrder(tree):
    if tree is not None:
        PostOrder(tree.first_child)
        Visit(tree)
        PostOrder(tree.next_sibling)

def main():
    tree = NewTreeNode()
    child = NewTreeNode()
    sibling = NewTreeNode()
    tree.first_child = child
    child.next_sibling = sibling
    PostOrder(tree)


main()