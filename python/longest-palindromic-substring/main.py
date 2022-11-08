# 给你一个字符串 s，找到 s 中最长的回文子串。
'''
输入：s = "babad"
babad
dabab
输出："bab"
解释："aba" 同样是符合题意的答案。

abab

首先需要判断什么是回文的串，然后再找最长的回文串
'''


# 中间扩散思路，从中间向外扩散
def longestPalindrome(s: str) -> str:
    maxLen = 0
    max_s = ''
    for i in range(len(s)):
        a = P(s, i, i)
        b = P(s, i, i + 1)
        cur = max(a, b)
        if a > b:
            cur_str = s[int(i - (a - 1) / 2): int(i + (a - 1) / 2 + 1)]
        else:
            cur_str = s[int(i -b / 2 + 1): int(i + b / 2 + 1)]
        if cur > maxLen:
            max_s = cur_str
            maxLen = cur
    return max_s


def P(s, left, right):
    i = left
    j = right
    while i >= 0 and j < len(s):
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            break

    return (j - 1) - (i + 1) + 1


# 本着找到最长的之后，下一次再找就会需要继续选择更加长的子串
def longestPalindrome2(s: str) -> str:
    max_s = ''
    for i in range(len(s)):
        for j in range(i + len(max_s), len(s) + 1):
            a = s[i:j]
            if huiwen(a) and len(a) > len(max_s):
                max_s = a
    return max_s


def huiwen(s: str):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    # print(longestPalindrome(
    #     'abaa'))
    print(longestPalindrome(
        'abba'))
    print(huiwen('aba'))
