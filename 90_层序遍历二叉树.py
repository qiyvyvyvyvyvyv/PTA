"""
给定链式队列类和二叉树类，本题要求实现层序遍历二叉树的函数
"""
class Node:
    def __init__(self, data, left_tree=None, right_tree=None):
        self.data = data
        self.left = left_tree
        self.right = right_tree

def CreateBinaryTree(value, left_tree=None, right_tree=None):
    tree = Node(value, left_tree, right_tree)
    return tree

def InitQueue():
    queue = []
    return queue

def EnQueue(queue, x):
    queue.append(x)

def DeQueue(queue):
    if (len(queue) > 0):
        data = queue.pop(0)
    else:
        print("stack is empty")
        data = None
    return data

def Peek(queue):  # 取队首元素
    if (len(queue) > 0):
        return queue[0]
    else:
        print("stack is empty")
        return None

def Visit(tree):
    print(tree.data)

def IsEmpty(queue):
    if (len(queue) == 0):
        return True
    else:
        return False

def DestroyQueue(queue):
    queue.clear()

def LevelOrder(tree):
    que = InitQueue()
    EnQueue(que, tree)
    while not IsEmpty(que):
        tree = DeQueue(que)
        Visit(tree)
        if tree.left is not None:
            EnQueue(que, tree.left)
        if tree.right is not None:
            EnQueue(que, tree.right)

def main():
    data = input()
    left = CreateBinaryTree(data)
    data = input()
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    LevelOrder(tree)


main()