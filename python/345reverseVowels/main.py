'''
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。


示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"

'''


def reverseVowels(s: str) -> str:
    candidate = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    i = 0
    j = len(s) - 1
    s = list(s)
    while i < j:
        if s[i] not in candidate:
            i += 1

        if s[j] not in candidate:
            j -= 1

        if s[i] in candidate and s[j] in candidate:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1

    return "".join(s)


if __name__ == '__main__':
    print(reverseVowels('holle'))
    print(reverseVowels('leetcode'))
