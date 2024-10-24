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


思考：
这个题目是求不重复的子串的长度，所以对于滑动窗口情况就不是一个定长的滑动窗口。可以用left和right来控制滑动窗口，
控制left的大小的条件就是子串中不能出现重复的字符，所以用一个Set来存放当前window中存在的字符；
从0开始迭代right，right增加，添加一个字符的时候，判断是否已经存在，如果已经存在，则left++;
直到right指定的字符能够放到滑动窗口的set中。然后更新结果。

总结：不定长滑动窗口
1. left = 0 ，维护一个滑动窗口
2. 从0开始迭代right
3. 判断是否满足题目要求，不满足要求，left++，直到满足题目要求；满足要求之后把right添加到窗口中
4. 更新结果
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