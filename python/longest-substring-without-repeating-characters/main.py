# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。
#
#
#
# 示例
# 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"abc"，所以其长度为 3。

# 无重复子串
def LongestSubstring(s: str) -> str:
    l = []
    for i in range(len(s)):
        a = s[i]
        for j in range(i + 1, len(s)):
            if s[j] not in a:
                a += s[j]
            else:
                break
        l.append(a)
    return l


# 无重复子序列
def Substring(s: str) -> str:
    result = ''
    for i in s:
        if i not in result:
            result += i
    return result


# 无重复子串
def lengthOfLongestSubstring(s: str) -> int:
    l = []
    for i in range(len(s)):
        a = s[i]
        for j in range(i + 1, len(s)):
            if s[j] not in a:
                a += s[j]
            else:
                break
        l.append(a)
    max = 0
    for item in l:
        if len(item) >= max:
            max = len(item)
    return max


if __name__ == '__main__':
    print(Substring('abcabacbbd'))
    print(lengthOfLongestSubstring('abcabacbb'))
