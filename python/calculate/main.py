'''
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。


输入：s = "1 + 1"
输出：2

输入：s = " 2-1 + 2 "
输出：3


输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
'''


def calculate(s: str, ) -> int:
    ops = [1]
    sign = 1

    ret = 0
    n = len(s)
    i = 0
    while i < n:
        if s[i] == ' ':
            i += 1
        elif s[i] == '+':
            sign = ops[-1]
            i += 1
        elif s[i] == '-':
            sign = -ops[-1]
            i += 1
        elif s[i] == '(':
            ops.append(sign)
            i += 1
        elif s[i] == ')':
            ops.pop()
            i += 1
        else:
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            ret += num * sign
    return ret


if __name__ == '__main__':
    print(calculate(" 2-1 + 2 "))
