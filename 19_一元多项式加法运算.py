"""
要求实现一个函数，函数接收两个PolyNode类的对象p1和p2。
函数通过遍历以p1和p2作为头节点的多项式链表得到两个多项式的和，返回多项式和的链表的头节点。
对于系数相同的两个节点求和时，指数不变，系数相加。
不需要考虑和链表只有一个节点的情况。(多项式节点以指数大小从大到小排序)
"""
class PolyNode:
    def __init__(self, coef, expon, nxt=None):
        self.coef = coef  # 系数
        self.expon = expon  # 指数
        self.next = nxt  # 线性表中下一个元素对象的引用


def Attach(coef, expon, rear):
    rear.next = PolyNode(coef, expon)  # 在rear后面新建一个结点
    rear = rear.next  # rear指向新的最后一个结点
    return rear


def ReadPoly():
    n = int(input())  # 读入多项式非零项个数
    p = PolyNode(0, 0)  # 创建临时空头结点
    rear = p  # rear指向多项式最后一个结点，初始化指向空头结点
    for _ in range(n):
        coef, expon = map(float, input().split())  # 读入每个非零项，按指数递减
        rear = Attach(coef, expon, rear)  # 新增非零项贴到多项式尾部
    temp = p
    p = p.next  # 令p指向结果多项式第一个非零项
    del temp
    return p


# 算法2-9：一元多项式加法运算  PolynomialAdd(p1, p2)
def PolynomialAdd(p1, p2):
    pass


# 算法2-9结束

def PrintPoly(p):
    current_node = p
    if p is None:
        print(0)
        return
    i = 1
    while current_node is not None and current_node.next is not None:
        if i == 1:
            print(f"{current_node.coef}x^ {int(current_node.expon)} ", end=' ')
            i += 1
        else:
            if current_node.coef != 0:
                if current_node.coef > 0:  # 输出正数
                    print(f"+ {current_node.coef}x^ {int(current_node.expon)} ", end=' ')
                else:  # 输出负数
                    print(f" {current_node.coef}x^ {int(current_node.expon)} ", end=' ')
        current_node = current_node.next
    if current_node and current_node.coef > 0:
        if i != 1: print("+ ", end="")
        if current_node.expon == 0 and current_node.coef != 0:
            print(f"{current_node.coef}  ")  # 最后1项是常数回车结束
        else:
            print(f"{current_node.coef}x^ {int(current_node.expon)}  ")  # 最后1项回车结束
    else:
        if current_node and current_node.coef != 0:
            if i != 1: print(" ", end="")
            if current_node.expon == 0:
                print(f"{current_node.coef}  ")  # 最后1项是常数回车结束
            else:
                print(f"{current_node.coef}x^ {int(current_node.expon)}  ")  # 最后1项非常数回车结束


def main():
    p1 = ReadPoly()
    p2 = ReadPoly()
    p = PolynomialAdd(p1, p2)
    PrintPoly(p)


main()