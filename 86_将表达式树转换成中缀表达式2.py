"""
表达式树 <-> 中缀表达式

核心思路：
  1. 中序遍历（左-根-右）保证操作数顺序正确；
  2. 括号由「子树根的优先级 vs 当前运算符优先级」决定，只在必需时添加。

两种实现：
  to_infix_str()   递归返回字符串，代码短、易读（作业/面试首选）
  to_infix_fast()  递归往缓冲区写，总复杂度 O(n)，适合超长表达式
另附一个小型递归下降解析器 parse_infix()，用于把中缀式子建成树（做验证/演示）。

三、加括号的判定规则（这是全部精髓）
先约定优先级：操作数 4（最高）、一元负号 3、* / 2、+ - 1。

位置	条件	是否加括号	例子
左子树	prec(左) < prec(op)	加	(a+b)*c
左子树	prec(左) >= prec(op)不加	(a-b)-c → a-b-c
右子树	prec(右) < prec(op)	加	a*(b+c)
右子树	prec(右) > prec(op)	不加	a+b*c
右子树	优先级相同且 op ∈ {- , /}	加	a-(b-c)、a/(b/c)
右子树	优先级相同且 op ∈ {+ , *}	不加	a+(b+c) → a+b+c
为什么左右不对称？因为二元运算符是左结合的：

左边同优先级，去掉括号后解析出来还是原来那棵树：(a-b)-c = a-b-c ✅
右边同优先级，去掉括号就变成了左结合：a-(b-c) → a-b-c = (a-b)-c ❌
而 +/* 可结合，a+(b+c) 和 a+b+c 数学上等价，可以去（要保留树的原形状就另说）
"""

# 优先级：数字越大结合越紧
P_ADD, P_MUL, P_NEG, P_NUM = 1, 2, 3, 4   # +- | */ | 一元负号 | 操作数


class Node:
    __slots__ = ("op", "left", "right", "val")

    def __init__(self, op=None, left=None, right=None, val=None):
        self.op = op            # None=叶子(操作数)，'neg'=一元负号
        self.left = left
        self.right = right
        self.val = val

    def __repr__(self):
        if self.op is None:
            return self.val
        if self.op == "neg":
            return f"(neg {self.left!r})"
        return f"({self.op} {self.left!r} {self.right!r})"


def prec_of(node: Node) -> int:
    """子树根运算符的优先级（叶子视为最高）。"""
    if node.op is None:
        return P_NUM
    if node.op == "neg":
        return P_NEG
    return P_MUL if node.op in ("*", "/") else P_ADD

def need_parens(child: Node, op: str, is_right: bool) -> bool:
    """child 作为 op 的左/右操作数时，是否必须套括号。"""
    pre = prec_of(child)

    if op == "neg":
        return pre <= P_NEG

    if is_right and op == "neg":
        return True

    p = P_MUL if op in ('*', '/') else P_ADD
    if pre < p:
        return True
    if pre > p:
        return False
    if not is_right:
        return False
    return op in ("-", "/")

# """child 作为 op 的左/右操作数时，是否必须套括号。"""
#     pc = prec_of(child)
#     if op == "neg":                      # 一元负号
#         return pc <= P_NEG               # -a 不加；-(a*b)、-(-a) 要加
#     # 右孩子是一元负号时一律加括号，避免写出 a--b / a*-b 这种粘连形式
#     if is_right and child.op == "neg":
#         return True
#     p = P_MUL if op in ("*", "/") else P_ADD
#     if pc < p:                           # 子式比当前运算符松 -> 必须加
#         return True
#     if pc > p:                           # 更紧 -> 不加
#         return False
#     # 优先级相同：左侧总能省（左结合，(a-b)-c == a-b-c）
#     if not is_right:
#         return False
#     # 右侧只有 + * 能省；(a-(b-c))、a/(b/c) 必须保留括号
#     return op in ("-", "/")
# --------------------------------------------------------------- 实现一
def to_infix_str(node: Node) -> str:
    return _walk(node)[0]


def _walk(node: Node) -> (str, int):
    """返回 (子式中缀串, 该子树根的优先级)。"""
    if node.op is None:
        return node.val, P_NUM

    if node.op == "neg":
        # (a-b)-c
        s, _ = _walk(node.left)
        if need_parens(node.left, "neg", False):
            s = f"(-{s})"
        return f"-{s}", P_NEG

    left, left_p = _walk(node.left)
    if need_parens(node.left, node.op, False):
        left = f"({left})"

    right, right_p = _walk(node.right)
    if need_parens(node.right, node.op, True):
        right = f"({right})"

    return f"{left}{node.op}{right}", prec_of(node)


# """返回 (子式中缀串, 该子树根的优先级)。"""
#     if node.op is None:
#         return node.val, P_NUM
#     if node.op == "neg":
#         s, _ = _walk(node.left)
#         if need_parens(node.left, "neg", False):
#             s = "(" + s + ")"
#         return "-" + s, P_NEG
#     ls, _ = _walk(node.left)
#     if need_parens(node.left, node.op, False):
#         ls = "(" + ls + ")"
#     rs, _ = _walk(node.right)
#     if need_parens(node.right, node.op, True):
#         rs = "(" + rs + ")"
#     return ls + node.op + rs, prec_of(node)
# --------------------------------------------------------------- 实现二
def to_infix_fast(node: Node) -> str:
    """写进缓冲区，避免 O(n^2) 的字符串拼接。"""
    out = []

    def go(u: Node):
        if u.op is None:
            out.append(u.val)
            return
        if u.op == "neg":
            wrap = need_parens(u.left, "neg", False)
            out.append("-")
            if wrap:
                out.append("(")
            go(u.left)
            if wrap:
                out.append(")")
            return
        wrap = need_parens(u.left, u.op, False)
        if wrap:
            out.append("(")
        go(u.left)
        if wrap:
            out.append(")")
        out.append(u.op)
        wrap = need_parens(u.right, u.op, True)
        if wrap:
            out.append("(")
        go(u.right)
        if wrap:
            out.append(")")

    go(node)
    return "".join(out)


# ------------------------------------------------- 附：中缀 -> 树（做验证用）
import re

_TOKEN = re.compile(r"\s*(\d+|[A-Za-z_]\w*|[+\-*/()])")


def tokenize(s: str):
    toks, pos = [], 0
    while pos < len(s):
        m = _TOKEN.match(s, pos)
        if not m:
            raise ValueError(f"无法识别: {s[pos:]!r}")
        toks.append(m.group(1))
        pos = m.end()
    return toks


class _Parser:
    def __init__(self, toks):
        self.t, self.i = toks, 0

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def expr(self):                      # expr := term (('+'|'-') term)*
        node = self.term()
        while self.peek() in ("+", "-"):
            op = self.t[self.i]; self.i += 1
            node = Node(op, node, self.term())
        return node

    def term(self):                      # term := factor (('*'|'/') factor)*
        node = self.factor()
        while self.peek() in ("*", "/"):
            op = self.t[self.i]; self.i += 1
            node = Node(op, node, self.factor())
        return node

    def factor(self):                    # factor := '-' factor | '(' expr ')' | NUM
        tk = self.peek()
        if tk == "-":
            self.i += 1
            return Node("neg", self.factor())
        if tk == "(":
            self.i += 1
            node = self.expr()
            if self.peek() != ")":
                raise ValueError("括号不匹配")
            self.i += 1
            return node
        if tk is None:
            raise ValueError("表达式意外结束")
        self.i += 1
        return Node(None, val=tk)


def parse_infix(s: str) -> Node:
    p = _Parser(tokenize(s))
    root = p.expr()
    if p.peek() is not None:
        raise ValueError(f"多余内容: {p.peek()}")
    return root


# --------------------------------------------------------------- 演示
if __name__ == "__main__":
    cases = [
        ("a+b*c", "a+b*c"),
        ("(a+b)*c", "(a+b)*c"),
        ("a-(b-c)", "a-(b-c)"),
        ("(a-b)-c", "a-b-c"),
        ("a/(b/c)", "a/(b/c)"),
        ("(a/b)/c", "a/b/c"),
        ("a+(b+c)", "a+b+c"),
        ("(a+b)*(c-d)", "(a+b)*(c-d)"),
        ("a+b+c+d", "a+b+c+d"),
        ("-(a+b)", "-(a+b)"),
        ("-a*b+12", "-a*b+12"),
    ]
    print(f"{'输入中缀':<14} {'树':<28} {'输出中缀':<16} 校验")
    for src, want in cases:
        root = parse_infix(src)
        got = to_infix_str(root)
        fast = to_infix_fast(root)
        ok = "OK" if got == want and fast == want else "!!"
        print(f"{src:<14} {root!r:<28} {got:<16} {ok}")