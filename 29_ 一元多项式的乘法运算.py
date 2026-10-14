"""
设计实现两个链式存储的一元多项式乘法运算的算法，并分析该算法的时间复杂度
"""
class PolyNode:
    def __init__(self, coef, expon):
        self.coef = coef  # 系数
        self.expon = expon  # 指数
        self.next = None  # 线性表中下一个元素对象的引用

def Attach(coef, expon, rear):
    rear.next = PolyNode(coef, expon)
    rear = rear.next
    return rear

def Multiply(p1, p2):
    """
    多项式乘法运算
    :param p1: 多项式1
    :param p2: 多项式2
    :return: 多项式乘积
    :时间复杂度: O(n^2)
    """
    if p1 is None or p2 is None:
        return PolyNode(0, 0)
    q1, q2 = p1, p2
    result_dict = {}  # 使用字典存储结果多项式的系数和指数
    while q1 is not None:
        while q2 is not None:
            coef = q1.coef * q2.coef
            expon = q1.expon + q2.expon
            if expon in result_dict:
                result_dict[expon] += coef
            else:
                result_dict[expon] = coef
            q2 = q2.next
        q1 = q1.next
        q2 = p2
    list = sorted(result_dict.keys(), reverse=True)  # 对结果多项式的指数进行排序
    p3 = PolyNode(result_dict[list[0]], list[0])  # 创建结果多项式的头结点
    rear = p3
    for i in range(1, len(list)):
        if result_dict[list[i]] != 0:
            rear = Attach(result_dict[list[i]], list[i], rear)
    return p3 if p3.coef != 0 else PolyNode(0, 0)

def ReadPoly():
    p = PolyNode(0, 0)  # 创建临时空头结点
    rear = p  # rear指向多项式最后一个结点，初始化指向空头结点
    rear.next = None
    data = list(map(int, input().split()))
    for i in range(data[0]): rear = Attach(data[2*i+1], data[2*i+2], rear)
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

if __name__ == '__main__':
    p1 = ReadPoly()
    p2 = ReadPoly()

    # 计算乘积多项式
    result = Multiply(p1, p2)

    # 输出结果多项式
    PrintPoly(result)