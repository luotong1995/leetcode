def decodeString(s: str) -> str:
    stack = []
    num_stack = []
    a = ''
    num = ''
    cur_num = 0
    for item in s:
        if not item.isdigit() and num:
            cur_num = int(num)
            num = ''
        if item.isdigit():
            num += item
            continue
        if item == '[':
            stack.append(a)
            num_stack.append(cur_num)
            a = ''
        elif item == ']':
            count = num_stack.pop()
            a = stack.pop() + ''.join([a for _ in range(count)])
        else:
            a += item
    return a


def decodeString2(s: str) -> str:
    i = 0
    stack = []

    def getDigit(s, index):
        sub = ''
        while s[index].isdigit():
            sub += s[index]
            index += 1
        return sub, index

    while i < len(s):
        c = s[i]
        if c.isdigit():
            sub, i = getDigit(s, i)
            stack.append(int(sub))
        elif c.isalpha() or c == '[':
            stack.append(c)
            i += 1
        else:
            i += 1
            a = []
            while stack[-1] != '[':
                a.append(stack.pop())
            a = a[::-1]
            a = ''.join([item for item in a])
            stack.pop()
            count = stack.pop()
            token = ''.join([a for _ in range(count)])
            stack.append(token)

    return ''.join([item for item in stack])


# print(decodeString2('32[a]2[bc]'))
# print(decodeString2('3[a2[c]]'))
print(decodeString2("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
# print(decodeString2('2[abc]3[cd]ef'))
# print(decodeString2('abc3[cd]xyz'))
