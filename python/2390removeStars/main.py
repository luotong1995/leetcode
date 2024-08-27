def removeStars(s: str) -> str:
    stack = []
    for item in s:
        if item == '*':
            stack.pop()
        else:
            stack.append(item)
    return ''.join(stack)


print(removeStars('leet**cod*e'))
