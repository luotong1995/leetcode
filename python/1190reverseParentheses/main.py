def reverseParentheses(s: str) -> str:
    stack = []
    result = list(s)

    for i, item in enumerate(s):
        if item == '(':
            stack.append((i))
        elif item == ')':
            start = stack.pop()
            temp = result[start + 1: i]
            temp.reverse()
            result[start + 1: i] = temp

    return ''.join([item for item in result if item not in ['(', ')']])


def reverseParentheses2(s: str) -> str:
    stack = []
    a = ''
    for item in s:
        if item == '(':
            stack.append(a)
            a = ''
        elif item == ')':
            a = stack.pop() + a[::-1]
        else:
            a += item
    return a


if __name__ == '__main__':
    # print(reverseParentheses('(u(love)i)'))
    a = 'dadsa'
    print()
    print(reverseParentheses2('(u(love)i)'))
