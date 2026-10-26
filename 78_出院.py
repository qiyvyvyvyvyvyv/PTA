"""
A：最近出了一个饮料营养等级你们知道吗？例如无糖的饮料是 A 级，可乐是 D 级……
B：那……无糖可乐是什么级别？
C：AD 级吧。
A：出院！
B：出什么院，你也给我进去！
以上是某群中一段有趣的对话。请你按照里面的逻辑，在已知某些饮料的等级的情况下，给饮料定级。定级的方法是：
如果是已知等级的饮料，直接输出等级；
对于一个新饮料的名字，你需要将名字拆成两个已知等级的部分，然后输出这个级别。例如：Diet是A，Coke是D，那么DietCoke就是AD；
如果新饮料无法拆解或者有多种拆解方法，统一定为 D 级。
输入格式：
输入第一行是两个正整数n和m(1≤n,m≤100)，表示已知的饮料有 n 种，需要定级的饮料有 m 种。
接下来首先是 n 行，每行是一个字符串和一个字符，表示一种饮料的名字和对应的等级，等级只有 A、B、C、D 四种。
然后是 m 行，每行是一个字符串，表示需要定级的饮料的名字。
所有饮料名字只包含有大小写字母，长度不超过 30，给定拥有等级的饮料的名字不会重复。
输出格式：
对于每一个需要定级的饮料，输出定好的定级。
"""
def assign_grades(n, m, known_drinks, drinks_to_grade):
    grades = []
    for drink in drinks_to_grade:
        if drink in known_drinks:              # 已知饮料：直接输出等级
            grades.append(known_drinks[drink])
            continue
        ways = []
        for k in range(1, len(drink)):         # 枚举每个字符间隙作为切分点
            left, right = drink[:k], drink[k:]
            if left in known_drinks and right in known_drinks:
                ways.append(known_drinks[left] + known_drinks[right])
        if len(ways) == 1:                     # 恰好一种拆法才采用
            grades.append(ways[0])
        else:                                  # 0种或多种拆法，都是D
            grades.append('D')
    return grades

if __name__ == '__main__':
    n, m = map(int, input().split())
    known_drinks = {}
    for _ in range(n):
        drink, grade = input().split()
        known_drinks[drink] = grade
    drinks_to_grade = []
    for _ in range(m):
        drinks_to_grade.append(input())
    grades = assign_grades(n, m, known_drinks, drinks_to_grade)
    for grade in grades:
        print(grade)