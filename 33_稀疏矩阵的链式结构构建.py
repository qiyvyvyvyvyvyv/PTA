"""
设计两个函数，一个函数根据读入的“行号 列号 元素值”三元组构建十字链表表示的稀疏矩阵，
另一个函数从矩阵中查询指定行列上元素的值
"""
class MatrixNode:
    def __init__(self, row, col, data):
        self.row = row # 行
        self.col = col # 列
        self.data = data # 元素值
        self.right = None # 右指针
        self.down = None # 下指针

class CrossLinkedList:
    def __init__(self, rows, cols):
        self.rows = rows # 行数
        self.cols = cols # 列数
        self.row_heads = [None] * rows # 行头指针
        self.col_heads = [None] * cols # 列头指针

def BuildSparseMatrix(n_row, n_col, n):
    matrix = CrossLinkedList(n_row, n_col)
    for _ in range(n):
        row, col, data = map(int, input().split())
        node = MatrixNode(row, col, data)
        if matrix.row_heads[row] is None:
            matrix.row_heads[row] = node
        else:
            current = matrix.row_heads[row]
            while current.right is not None:
                current = current.right
            current.right = node

        if matrix.col_heads[col] is None:
            matrix.col_heads[col] = node
        else:
            current = matrix.col_heads[col]
            while current.down is not None:
                current = current.down
            current.down = node
    return matrix
    # matrix = CrossLinkedList(n_row, n_col)
    # right_dict = {}
    # down_dict = {}
    # for _ in range(n):
    #     row, col, data = map(int, input().split())
    #     if row not in right_dict:
    #         right_dict[row] = [[col, data]]
    #     else:
    #         right_dict[row].append([col, data])
    #
    #     if col not in down_dict:
    #         down_dict[col] = [[row, data]]
    #     else:
    #         down_dict[col].append([row, data])
    # for row in right_dict.keys():
    #     a_list = right_dict[row]
    #     for col, data in a_list:
    #         node = MatrixNode(row, col, data)
    #         if matrix.row_heads[row] is None:
    #             matrix.row_heads[row] = node
    #         else:
    #             current = matrix.row_heads[row]
    #             while current.right is not None:
    #                 current = current.right
    #             current.right = node
    #
    # for col in down_dict.keys():
    #     a_list = down_dict[col]
    #     for row, data in a_list:
    #         node = MatrixNode(row, col, data)
    #         if matrix.col_heads[col] is None:
    #             matrix.col_heads[col] = node
    #         else:
    #             current = matrix.col_heads[col]
    #             while current.down is not None:
    #                 current = current.down
    #             current.down = node

def GetElem(matrix, row, col):
    if row < 0 or row >= matrix.rows or col < 0 or col >= matrix.cols:
        print("ERROR")
        return 0
    current = matrix.row_heads[row]
    while current is not None and current.col < col:
        current = current.right
    if current is not None and current.col == col:
        return current.data
    else:
        return 0

if __name__ == "__main__":
    n_row, n_col, n = map(int, input().split())
    sparse_matrix = BuildSparseMatrix(n_row, n_col, n)

    row, col = map(int, input().split())
    print(GetElem(sparse_matrix, row, col))
