'''
3. 无重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成
'''


def lengthOfLongestSubstring(s: str) -> int:
    ans = 0
    left = 0
    a = set()
    for right in range(len(s)):
        while s[right] in a:
            a.remove(s[left])
            left += 1
        a.add(s[right])
        ans = max(ans, right - left + 1)
    return ans
s = "abcabcbb"
print(lengthOfLongestSubstring(s))