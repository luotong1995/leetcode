'''
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
输入：s = "bcabc"
输出："abc"
'''
import collections


# 使用单调栈来完成

def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    counter = collections.Counter(s)
    for item in s:
        if item not in stack:
            while stack and item < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(item)
        counter[item] -= 1
    return ''.join(stack)


if __name__ == '__main__':
    print(removeDuplicateLetters('cbacdcbc'))
