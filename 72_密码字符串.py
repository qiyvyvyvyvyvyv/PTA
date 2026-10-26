"""
给定一个密码字符串 password，
其中可能包含大写英文字母、小写英文字母、数字或特殊符号（如！、@、# 等）。
若密码中存在至少一个字母同时出现小写形式和大写形式（例如同时存在 'a' 和 'A'），
则称该密码包含 “大小写混合字母”。请判断该密码包含 “大小写混合字母”的个数
"""
def main():
    s = input()
    count = 0
    s_dict = {}
    for i in s:
        if i.islower():
            if i.upper() in s_dict and i not in s_dict:
                count += 1
            s_dict[i] = 1
        elif i.isupper():
            if i.lower() in s_dict and i not in s_dict:
                count += 1
            s_dict[i] = 1
    print(count)

if __name__ == "__main__":
    main()