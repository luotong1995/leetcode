'''
76. 最小覆盖子串

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

 

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
 

提示：

m == s.length
n == t.length
1 <= m, n <= 10^5
s 和 t 由英文字母组成

思考：
还是用滑动窗口来求最小；
还是按照固定RIGHT来不断移动left的位置，求出最小的window，当加入一个right的时候去判断，减去left能否满足当前的要求，如果能满足则left++，不能满足即为当前RIGHT情况的最小的window

while left < len(s) and (s[left] not in t or cnt[s[left]] < 0)
这里就是不断的移动left，条件就是left不能超过s的长度且s[left]不在t中可以直接left++，或者需要cnt[s[left]] < 0 (当前窗口已经存在s[left]了)
然后更新最小值ans=min(right-left+1,ans)

'''


from typing import Counter


def minWindow(s: str, t: str) -> str:
    ans = ""
    mid_ans = len(s) + 1
    left = 0
    cnt = Counter()
    for item in t:
        cnt[item] += 1
    for right in range(len(s)):
        if s[right] in cnt:
            cnt[s[right]] -= 1
        while left < len(s) and (s[left] not in t or cnt[s[left]] < 0):
            if s[left] in t:
                cnt[s[left]] += 1
            left += 1
        if all([v <=0 for _, v in cnt.items()]):
            if right - left + 1 < mid_ans:
                ans = s[left:right+1]
            mid_ans = min(mid_ans, right - left + 1)
    if mid_ans == len(s) + 1:
        return ""
    else:
        return ans

# print(minWindow("ADOBECODEBANC", "ABC"))
# print(minWindow("a", "aa"))
# print(minWindow("a", "b"))
print(minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))