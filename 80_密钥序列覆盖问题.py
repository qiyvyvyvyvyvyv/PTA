"""
某加密算法要求密钥序列需覆盖所有k位二进制组合，以确保加密强度。
给定二进制密钥字符串s和整数k，请检查s是否包含所有可能的k位二进制子串（即所有2^k种组合）。
若满足则返回True（密钥有效），否则返回False（存在安全漏洞）
"""
def main():
    s = input()
    the_len = int(input())
    the_sum = 2 ** the_len
    a_dict = {}
    for i in range(len(s) - the_len + 1):
        if s[i:i+the_len] not in a_dict:
            a_dict[s[i:i+the_len]] = 1
        else:
            a_dict[s[i:i+the_len]] += 1
    if len(a_dict) == the_sum:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()