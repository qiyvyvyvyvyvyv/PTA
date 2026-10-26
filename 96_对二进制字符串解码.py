"""
给定链表类和二叉哈夫曼树类和哈夫曼树生成方法，本题要求实现一个能根据传入的哈夫曼树和二进制字符串解码生成正确的字符集的函数
"""
# 定义哈夫曼树
class BinaryTreeNode:
    def __init__(self, weight=0, data='', left_tree=None, right_tree=None) -> None:
        self.weight = weight  # 权重
        self.data = data  # 字符
        self.left = left_tree  # 左子树指针
        self.right = right_tree  # 右子树指针

# 树的集合的定义，即树结点的单链表
class SetNode():
    def __init__(self, data=None, next=None) -> None:
        self.data: BinaryTreeNode = data  # 存储数据
        self.next = next  # 指向线性表中下一个元素

class HeadNode():
    def __init__(self) -> None:
        self.head = None  # 单链表头指针
        self.length = 0  # 表长

    # 将一个树节点插入链表头部
    def Insert(self, tree: BinaryTreeNode):
        p = SetNode(tree)
        p.next = self.head
        self.head = p
        self.length += 1

    # 删除并返回链表中最小权重的树节点
    def ExtrectMin(self):
        if self.length == 0: return None  # 空集则返回空指针
        # 方便起见加一个临时头结点
        tmpHeadNode = SetNode()
        tmpHeadNode.next = self.head
        self.head = tmpHeadNode
        # 初始化最小值为第1个结点，preMinp为空头结点
        preMinp = tmpHeadNode
        p = tmpHeadNode.next
        minWeight = p.data.weight
        while p.next != None:
            if p.next.data.weight < minWeight:  # 若下一个结点值更小
                minWeight = p.next.data.weight
                preMinp = p
            p = p.next
        p = preMinp.next  # p指向最小值结点
        preMinp.next = p.next  # 删除preMinp后面的结点
        self.length -= 1
        tree = p.data
        self.head = tmpHeadNode.next  # 删除临时空头结点
        return tree

# 算法5-15：创建哈夫曼树 CreateHuffmanTree(w)
def CreateHuffmanTree(weightList, charList):
    treeSet = HeadNode()  # 二叉树集合的初始化
    for i in range(len(weightList)):
        treeNode = BinaryTreeNode(weightList[i], charList[i])  # 创建叶节点
        treeSet.Insert(treeNode)  # 将新建节点插入树节点链表中
    for i in range(1, len(weightList)):  # 合并二叉树，共n-1次
        root = BinaryTreeNode()  # 新建树根结点
        root.left = treeSet.ExtrectMin()  # 取出根权重最小树作为左子树
        root.right = treeSet.ExtrectMin()  # 取出根权重最小树作为右子树
        if root.left == None:
            leftWeight = 0
        else:
            leftWeight = root.left.weight
        if root.right == None:
            rightWeight = 0
        else:
            rightWeight = root.right.weight
        root.weight = leftWeight + rightWeight  # 设置新树的根权重
        treeSet.Insert(root)
    tree = treeSet.ExtrectMin()  # 取出集合中唯一的二叉树，即哈夫曼树
    return tree

# 算法5-15 结束
def Decoding(tree, binary_code):
    p = tree
    i = 0
    while i < len(binary_code):
        if binary_code[i] == '0':
            if p.left.data != '':
                print(p.left.data, end=" ")
                p = tree
            else:
                p = p.left
            i += 1
        elif binary_code[i] == '1':
            if p.right.data != '':
                print(p.right.data, end=" ")
                p = tree
            else:
                p = p.right
            i += 1
        else:
            i += 1

def main():
    weightList = [int(i) for i in input().split()]
    charList = input().split()
    binaryCode = input()
    tree = CreateHuffmanTree(weightList, charList)
    Decoding(tree, binaryCode)

main()
