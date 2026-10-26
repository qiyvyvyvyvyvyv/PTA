"""
给定链表类和二叉哈夫曼树类，本题要求实现一个能根据输入的权重列表生成并返回一颗哈夫曼树的函数
"""
import heapq
class BinaryTreeNode:
    def __init__(self, weight, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):  # 用于类对象的比较
        return self.weight < other.weight

def CreateBinaryTree(value, left_tree=None, right_tree=None):
    tree = BinaryTreeNode(value, left_tree, right_tree)
    return tree

def CreateHuffmanTree(w):
    if not w:
        return CreateBinaryTree(0)
    heap = [CreateBinaryTree(x) for x in w]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, CreateBinaryTree(left.weight + right.weight, left, right))
    return heap[0]

def WPL(tree, depth):  # 根据Huffman树计算编码总长度
    if tree.left == None:  # 是叶子结点
        return (depth * tree.weight)
    else:  # 否则一定有2个孩子
        return (WPL(tree.left, depth + 1) + WPL(tree.right, depth + 1))

def main():
    w = list(map(int, input().split()))  # 将空格分隔的输入整数存储在列表中
    tree = CreateHuffmanTree(w)
    print(WPL(tree, 0))


main()