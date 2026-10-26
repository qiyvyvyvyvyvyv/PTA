"""
给定链表队列类和二叉树类，本题要求实现一个能根据层序序列重构二叉树的函数。(序列中#表空节点)
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
    print(tree.data, end=" ")

def IsEmpty(queue):
    if (len(queue) == 0):
        return True
    else:
        return False

def DestroyQueue(queue):
    queue.clear()

def LevelOrder(tree):
    queue = InitQueue()
    EnQueue(queue, tree)
    while IsEmpty(queue) == False:
        node = DeQueue(queue)
        if node != None:
            Visit(node)
            EnQueue(queue, node.left)
            EnQueue(queue, node.right)

def LevelOrderDeSerialize(levelorder, n):
    que = InitQueue()
    if n == 0 or levelorder[0] == '#':
        return None
    levelorder = levelorder.split() if any(ch.isspace() for ch in levelorder) else list(levelorder)
    root = CreateBinaryTree(levelorder[0])
    EnQueue(que, root)
    i = 1

    while i < n:
        node = DeQueue(que)
        if node != None:
            if levelorder[i] != '#':
                node.left = CreateBinaryTree(levelorder[i])
                EnQueue(que, node.left)
            i += 1
            if i < n and levelorder[i] != '#':
                node.right = CreateBinaryTree(levelorder[i])
                EnQueue(que, node.right)
            i += 1
    return root

def main():
    levelorder = input()
    tree = LevelOrderDeSerialize(levelorder, len(levelorder))
    LevelOrder(tree)


main()