'''
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。
 

示例 1：

输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
示例 2：

输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
示例 3：

输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3
示例 4：

输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0
 

提示：

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s 只包含小写英文字母。

思考：要判断子串出现的次数，长度有限制，子串中不同元素的数量也有限制，暴力求解


方法一的时间复杂度较高，上文给出的代码刚好可以在规定时间内通过所有数据，那么我们是否可以进行一些优化呢？

假设字符串 T 在给定的字符串 S 中出现的次数为 k，那么 T 的任意一个子串出现的次数至少也为 k，即 T 的任意一个子串在 S 中出现的次数不会少于 T 本身。这样我们就可以断定，在所有满足条件且出现次数最多的的字符串中，一定有一个的长度恰好为 minSize。

我们可以使用反证法证明上述的结论：假设所有满足条件且出现次数最多的字符串中没有长度为 minSize 的，不妨任取其中的一个长度为 l 的字符串，根据假设，有 l > minSize。此时我们再任取该字符串的一个长度为 minSize 的子串，子串出现的次数不会少于原字符串出现的次数，与假设相矛盾。

这样以来，我们只需要枚举所有长度为 minSize 的字符串即可，时空复杂度均减少了 O(S)。

'''


from typing import Counter


def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    n = len(s)
    ans = 0
    cnt = Counter()
    for i in range(n):
        exist = set()
        cur = ''
        for j in range(i, min(n, i + maxSize)):
            exist.add(s[j])
            if len(exist) > maxLetters:
                break
            cur += s[j]
            if j - i + 1 >= minSize:
                cnt[cur] += 1
                ans = max(ans, cnt[cur])
    return ans

def maxFreq2(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    n = len(s)
    ans = 0
    cnt = Counter()
    for i in range(n - minSize + 1):
        cur = s[i: i + minSize]
        exist = set(cur)
        if len(exist) <= maxLetters:
            cnt[cur] += 1
            ans = max(ans, cnt[cur])
    return ans



s = "aabcabcab"
maxLetters = 2
minSize = 2
maxSize = 3
print(maxFreq2(s,maxLetters, minSize, maxSize))

