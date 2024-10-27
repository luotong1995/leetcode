'''

给你一个下标从 0 开始的字符串 s ，这个字符串只包含 0 到 9 的数字字符。
如果一个字符串 t 中至多有一对相邻字符是相等的，那么称这个字符串 t 是 半重复的 。例如，"0010" 、"002020" 、"0123" 、"2002" 和 "54944" 是半重复字符串，而 "00101022" （相邻的相同数字对是 00 和 22）和 "1101234883" （相邻的相同数字对是 11 和 88）不是半重复字符串。

 

示例 1：

输入：s = "52233"

输出：4

解释：

最长的半重复子字符串是 "5223"。整个字符串 "52233" 有两个相邻的相同数字对 22 和 33，但最多只能选取一个。

示例 2：

输入：s = "5494"

输出：4

解释：

s 是一个半重复字符串。

示例 3：

输入：s = "1111111"

输出：2

解释：

最长的半重复子字符串是 "11"。子字符串 "111" 有两个相邻的相同数字对，但最多允许选取一个。

 

提示：

1 <= s.length <= 50
'0' <= s[i] <= '9'


思考：
至多有一对相邻的字符相等，就是0对和1对都行。

这里的条件就是至多1对相邻字符相等；然后求最长的子字符串，也是要用变长滑动窗口来做；
1. left=0
2. right 0~n-1
3. 如果满足 相邻字符对数量超过1，则left++
4. 更新结果	ans = max(right-left,ans)
'''


def longestSemiRepetitiveSubstring(s: str) -> int:
    left = 0
    ans = 0
    cur_pair = 0
    for right in range(len(s)):
        while right > 0 and cur_pair + (1 if s[right] == s[right - 1] else 0) > 1:
            cur_pair -= (1 if s[left] == s[left + 1] else 0)
            left += 1
        if right > 0:
            cur_pair += (1 if s[right] == s[right - 1] else 0)
        ans = max(right - left + 1, ans)
    return ans

def longestSemiRepetitiveSubstring2(s: str) -> int:
    left = 0
    ans = 1
    cur_pair = 0
    for right in range(1, len(s)):
        cur_pair += s[right] == s[right - 1]
        while cur_pair > 1:
            cur_pair -= s[left] == s[left + 1]
            left += 1
        ans = max(right - left + 1, ans)
    return ans


print(longestSemiRepetitiveSubstring("52233"))
print(longestSemiRepetitiveSubstring2("52233"))
print(longestSemiRepetitiveSubstring("5494"))
print(longestSemiRepetitiveSubstring2("5494"))
print(longestSemiRepetitiveSubstring("11"))
print(longestSemiRepetitiveSubstring2("11"))
print(longestSemiRepetitiveSubstring("0"))
print(longestSemiRepetitiveSubstring2("0"))