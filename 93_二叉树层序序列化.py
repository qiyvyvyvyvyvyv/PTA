"""
给定链式队列类和二叉树类，本题要求实现将二叉树层序序列化的函数。(输出特殊符号’#’代表空节点)
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
        print("queue is empty")
        data = None
    return data

def Peek(queue):  # 取队首元素
    if (len(queue) > 0):
        return queue[0]
    else:
        print("queue is empty")
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

def LevelOrderSerialize(tree):
    que = InitQueue()
    EnQueue(que, tree)
    while not IsEmpty(que):
        tree = DeQueue(que)
        if tree is not None:
            print(tree.data)
            EnQueue(que, tree.left)
            EnQueue(que, tree.right)
        else:
            print("#")

def main():
    data = input()
    left = CreateBinaryTree(data)
    data = input()
    right = CreateBinaryTree(data)
    data = input()
    tree = CreateBinaryTree(data, left, right)
    LevelOrderSerialize(tree)


main()