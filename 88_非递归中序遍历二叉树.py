"""
给定链式栈类和二叉树类，本题要求实现采用非递归方法中序遍历二叉树的函数
"""
class Node:
    def __init__(self, data, left_tree=None, right_tree=None):
        self.data = data
        self.left = left_tree
        self.right = right_tree

def CreateBinaryTree(value, left_tree=None, right_tree=None):
    tree = Node(value, left_tree, right_tree)
    return tree

def InitStack():
    stack = []
    return stack

def Push(stack, x):
    stack.append(x)

def Pop(stack):
    if (len(stack) > 0):
        stack.pop()
    else:
        print("stack is empty")

def Top(stack):
    if (len(stack) > 0):
        return stack[-1]
    else:
        print("stack is empty")
        return None

def Visit(tree):
    print(tree.data)

def IsEmpty(stack):
    if (len(stack) == 0):
        return True
    else:
        return False

def DestroyStack(stack):
    stack.clear()

def InOrder(tree):
    stack = InitStack()
    Push(stack, tree)
    while not IsEmpty(stack):
        tree = Top(stack)
        if tree.left is None:
            Visit(tree)
            Pop(stack)
            if tree.right is not None:
                Push(stack, tree.right)
        else:
            Push(stack, tree.left)
            tree.left = None

def main():
    data = input()
    left = CreateBinaryTree(data)
    data = input()
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    InOrder(tree)


main()