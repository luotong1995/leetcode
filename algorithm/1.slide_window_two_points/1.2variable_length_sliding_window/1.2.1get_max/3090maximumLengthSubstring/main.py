'''
3090. 每个字符最多出现两次的最长子字符串

给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该
子字符串的 最大 长度。
 

示例 1：

输入： s = "bcbbbcba"

输出： 4

解释：

以下子字符串长度为 4，并且每个字符最多出现两次："bcbb bcba"。

示例 2：

输入： s = "aaaa"

输出： 2

解释：

以下子字符串长度为 2，并且每个字符最多出现两次："aa aa"。



提示：

2 <= s.length <= 100
s 仅由小写英文字母组成。


思考：
这题也是不定长滑动窗口，然后求最大，所以还是需要用，left，right来维护滑动窗口。
然后这里的条件是，保证每个字符出现的次数不超过两次，所以这里用dict来维护数据，key为字符，value为出现的次数，控制在2次以内。
同样的初始化left为0，迭代right从0开始，然后加入right的时候需要判断是否存在，并且长度是否大于2，如果大于2，则讲left的删除，left++，知道能讲right加进去为止

最后求最大的长度

'''
from collections import defaultdict

def maximumLengthSubstring(s: str) -> int:
    left = 0
    w_dict = defaultdict(int)
    ans = 0
    for right in range(len(s)):
        while w_dict[s[right]] >= 2:
            w_dict[s[left]] -= 1
            left += 1
        w_dict[s[right]] += 1
        ans = max(ans, right - left + 1)
    return ans

print(maximumLengthSubstring('bcbbbcba'))