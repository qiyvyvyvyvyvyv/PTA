"""
开发一个化学配方智能解析系统，输入标准化学分子式，自动计算并输出每种原子的精确数量，用于实验室的原料需求分析和成本评估。
规则：
a. 原子名称以大写字母开头，后跟0个或多个小写字母（如H, Mg, Fe）。
b. 若原子后有数字，则表示该原子的数量（如H2表示2个氢原子）；若省略数字，则默认为1。
c. 括号 ()可嵌套，括号后的数字表示括号内所有原子的重复次数（如 (OH)2 表示2 个 O和2个H）
K4(ON(SO3)2)2
K4 N2 O14 S4
"""
def main():
    mol = list(input())
    n = len(mol)
    stack = [{}]
    i = 0
    while i < n:
        char = mol[i]
        if char == '(':
            stack.append({})
            i += 1
        elif char == ')':
            mol_dict = stack.pop()
            i += 1
            start = i
            while i < n and mol[i].isdigit():
                i += 1
            mul = int(''.join(mol[start:i])) if i > start else 1
            for key, value in mol_dict.items():
                stack[-1][key] = stack[-1].get(key, 0) + value * mul
        elif char.isupper():
            start = i
            i += 1
            while i < n and mol[i].islower():
                i += 1
            m = ''.join(mol[start:i])
            start = i
            while i < n and mol[i].isdigit():
                i += 1
            mul = int(''.join(mol[start:i])) if i > start else 1
            stack[-1][m] = stack[-1].get(m, 0) + mul
        else:
            i += 1

    result = stack[0]
    for key in sorted(result.keys()):
        item = result[key]
        if item > 1:
            print(key + str(item), end='')
        else:
            print(key, end='')

    # class Stack:
    #     def __init__(self, KMaxSize):
    #         self.KMaxSize = KMaxSize
    #         self.size = 0
    #         self.top = -1
    #         self.data = [0] * self.KMaxSize
    #
    #     def isFull(self):
    #         return self.size == self.KMaxSize
    #
    #     def isEmpty(self):
    #         return self.size == 0
    #
    #     def pop(self):
    #         if self.isEmpty():
    #             return None
    #         else:
    #             self.data[self.top] = 0
    #             self.top -= 1
    #             self.size -= 1
    #
    #     def getTop(self):
    #         if self.isEmpty():
    #             return None
    #         else:
    #             return self.data[self.top]
    #
    #     def push(self, item):
    #         if self.isFull():
    #             return None
    #         else:
    #             self.top += 1
    #             self.data[self.top] = item
    #             self.size += 1
    #
    # def main():
    #     mol = list(input())
    #     stack = Stack(len(mol))
    #     result_dict = {}
    #     num = 0
    #     while mol:
    #         char = mol.pop(0)
    #         if char.islower():
    #             # 小写字母直接压入栈 比如遇见 MgSO4
    #             stack.push(char)
    #         elif char.isupper():
    #             # 大写字母如果栈如为空 直接压入 如果括号对数量大于0 也直接压入 需要处理K4(ON(SO3)2)2
    #             if stack.isEmpty() or num != 0:
    #                 stack.push(char)
    #                 continue
    #             # 走到这说明栈里有元素 此时遇见大写字母需要直接弹出栈里所有元素 并且暗含条件 在此之前的原子数量为1
    #             string_list = []
    #             while not stack.isEmpty():
    #                 string_list.insert(0, stack.getTop())
    #                 stack.pop()
    #             if ''.join(string_list) in result_dict:
    #                 result_dict[''.join(string_list)] += 1
    #             else:
    #                 result_dict[''.join(string_list)] = 1
    #             stack.push(char)
    #         elif char.isdigit():
    #             # 如果括号对数量大于0 则直接压入栈 比如遇见 K4(ON(SO3)2)2 进行特殊处理
    #             if num != 0:
    #                 stack.push(char)
    #                 continue
    #             # 如果遇见数字说明 在此之前的原子数量为改数字 此外还需要注意 我们这里是单字符处理 因此要额外处理H14这种情况
    #             n = char
    #             while mol and mol[0].isdigit():
    #                 n += mol.pop(0)
    #             string_list = []
    #             while not stack.isEmpty():
    #                 string_list.insert(0, stack.getTop())
    #                 stack.pop()
    #             if ''.join(string_list) in result_dict:
    #                 result_dict[''.join(string_list)] += int(n)
    #             else:
    #                 result_dict[''.join(string_list)] = int(n)
    #         elif char == '(':
    #             # 如果遇见左括号 则将栈里所有元素弹出 并且暗含条件 在此之前的原子数量为1
    #             string_list = []
    #             while not stack.isEmpty() and num == 0:
    #                 string_list.insert(0, stack.getTop())
    #                 stack.pop()
    #             if string_list:
    #                 if ''.join(string_list) in result_dict:
    #                     result_dict[''.join(string_list)] += 1
    #                 else:
    #                     result_dict[''.join(string_list)] = 1
    #             stack.push(char)
    #             num += 1
    #         elif char == ')':
    #             # 如果遇见右括号 则将栈里所有元素弹出 直到遇见左括号 并且暗含条件 此时原子数量为括号前数字乘以括号内原子数量
    #             # K(OH)2
    #             if mol[0].isdigit() and num == 1:
    #                 string_list: list[str] = []
    #                 while stack.getTop() != '(':
    #                     string_list.insert(0, stack.getTop())
    #                     stack.pop()
    #                 # string_list = ['O', 'H']
    #                 # 删除 '('
    #                 stack.pop()
    #                 # 消减括号对数量
    #                 num -= 1
    #                 # 得到倍数
    #                 mul = mol.pop(0)
    #                 while mol and mol[0].isdigit():
    #                     mul += mol.pop(0)
    #                 mul = int(mul)
    #                 buffer_list = []
    #                 # string_list = ['O', 'H'] | ['O','4']
    #                 for i in range(len(string_list)):
    #                     if not buffer_list:
    #                         buffer_list.append(string_list[i])
    #                     elif string_list[i].isdigit():
    #                         if ''.join(buffer_list) in result_dict:
    #                             result_dict[''.join(buffer_list)] += mul * int(string_list[i])
    #                         else:
    #                             result_dict[''.join(buffer_list)] = mul * int(string_list[i])
    #                         buffer_list = []
    #                     elif string_list[i].isupper():
    #                         # buffer_list = ['O']
    #                         if ''.join(buffer_list) in result_dict:
    #                             result_dict[''.join(buffer_list)] += mul
    #                         else:
    #                             result_dict[''.join(buffer_list)] = mul
    #                         buffer_list = [string_list[i]]
    #                     elif string_list[i].islower():
    #                         buffer_list.append(string_list[i])
    #                 if buffer_list:
    #                     name = ''.join(buffer_list)
    #                     if name in result_dict:
    #                         result_dict[name] += mul
    #                     else:
    #                         result_dict[name] = mul
    #             # K4(ON(SO3)2)2
    #             elif mol[0].isdigit() and num > 1:
    #                 string_list: list[str] = []
    #                 while stack.getTop() != '(':
    #                     string_list.insert(0, stack.getTop())
    #                     stack.pop()
    #                 # stack.data = ['O','N','('] string_list = ['S','O','3']
    #                 # 删除 '('
    #                 stack.pop()
    #                 # 减少括号对数量
    #                 num -= 1
    #                 # 得到倍数
    #                 mul = mol.pop(0)
    #                 while mol and mol[0].isdigit():
    #                     mul += mol.pop(0)
    #                 mul = int(mul)
    #                 buffer_list = []
    #                 for i in range(len(string_list)):
    #                     # stack.data = ['O','N'] string_list = ['S','O','3']
    #                     if not buffer_list:
    #                         buffer_list.append(string_list[i])
    #                     elif string_list[i].isdigit():
    #                         buffer_list.append(str(mul * int(string_list[i])))
    #                     elif string_list[i].isupper():
    #                         buffer_list.append(str(mul))
    #                         buffer_list.append(string_list[i])
    #                     elif string_list[i].islower():
    #                         buffer_list.append(string_list[i])
    #                 for i in range(len(buffer_list)):
    #                     stack.push(buffer_list[i])
    #     tail = []
    #     while not stack.isEmpty():
    #         tail.insert(0, stack.getTop())
    #         stack.pop()
    #     if tail:
    #         name = ''.join(tail)
    #         result_dict[name] = result_dict.get(name, 0) + 1
    #     for key in sorted(result_dict.keys()):
    #         item = result_dict[key]
    #         if item > 1:
    #             print(key + str(item), end='')
    #         else:
    #             print(key, end='')

if __name__ == "__main__":
    main()