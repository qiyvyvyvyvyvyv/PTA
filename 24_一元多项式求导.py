"""
设计函数求一元多项式的导数。
输入格式：
以指数递降方式输入多项式非零项系数和指数（绝对值均为不超过1000的整数）。数字间以空格分隔。
输出格式：
以与输入相同的格式输出导数多项式非零项的系数和指数。数字间以空格分隔，但结尾不能有多余空格
"""
class PolyNode:
    def __init__(self, coef, expon):
        self.coef = coef
        self.expon = expon
        self.next = None

def Attach(coef, expon, rear):
    rear.next = PolyNode(coef, expon)
    rear = rear.next
    return rear

def ReadPoly():
    p = PolyNode(0, 0)  # 创建临时空头结点
    rear = p  # rear指向多项式最后一个结点，初始化指向空头结点
    rear.next = None
    while True:
        try:
            coef, expon = map(int, input().split())
            # 读入当前项系数和指数，直到文件结尾
            rear = Attach(coef, expon, rear)
            # 新增非零项贴到多项式尾部
        except Exception:
            break
    temp = p
    p = p.next  # 令p指向结果多项式第一个非零项
    del temp  # 清除临时空头结点
    return p

def PrintPoly(p):
    flag = 0  # 辅助调整输出格式用
    while p != None:
        if not flag:
            flag = 1
        else:
            print(" ", end="")
        print("%d %d" % (p.coef, p.expon), end="")
        p = p.next
    print()

def PolyDifferentiation(p):
    # 求多项式p的导函数，返回结果多项式
    # 原多项式在求导后即被导函数取代
    node = p
    pre_node = PolyNode(0, 0)
    pre_node.next = p
    while node is not None:
        if node.expon == 0 or node.coef == 0:
            if node.next is not None:
                node.next = node.next.next
                node = node.next
            else:
                if node == p:
                    p.coef = 0
                    p.expon = 0
                    node = None
                else:
                    pre_node.next = None
                    node = None
        else:
            node.coef *= node.expon
            node.expon -= 1
            pre_node = node
            node = node.next
    return p

def main():
    p = ReadPoly()
    PolyDifferentiation(p)
    PrintPoly(p)
main()