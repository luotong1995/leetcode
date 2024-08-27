def isValid(s: str) -> bool:
    stack = []
    for item in s:
        if item not in ['(', ')', '{', '}', '[', ']']:
            return False
        if item in ['(', '{', '[', ]:
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            else:
                if item == ')' and stack.pop() != '(':
                    return False
                elif item == ']' and stack.pop() != '[':
                    return False
                elif item == '}' and stack.pop() != '{':
                    return False
    return len(stack) == 0


# 加入？可以不用判断stack是否为空
def isValid2(s: str) -> bool:
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1


# print(isValid(']'))
print(isValid2(']'))
