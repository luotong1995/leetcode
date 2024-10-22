'''
2982 找出出现至少三次的最长特殊子字符串II

给你一个仅由小写英文字母组成的字符串 s 。

如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 "abc" 不是特殊字符串，而字符串 "ddd"、"zz" 和 "f" 是特殊字符串。

返回在 s 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 -1 。

子字符串 是字符串中的一个连续 非空 字符序列。

 

示例 1：

输入：s = "aaaa"
输出：2
解释：出现三次的最长特殊子字符串是 "aa" ：子字符串 "|aa|aa"、"a|aa|a" 和 "aa|aa|"。
可以证明最大长度是 2 。
示例 2：

输入：s = "abcdef"
输出：-1
解释：不存在出现至少三次的特殊子字符串。因此返回 -1 。
示例 3：

输入：s = "abcaba"
输出：1
解释：出现三次的最长特殊子字符串是 "a" ：子字符串 "abcaba"、"abcaba" 和 "abcaba"。
可以证明最大长度是 1 。


思考：
统计每个字母在字符串中，每段的连续长度。使用dict来进行存储，key为字符，value为list，里面的值为每段的连续的数量
根据这个dict，给定一个k(特殊子字符串),可以算出子字符串的长度为max(0, l-k+1) l为连续的子字符串的长度。
条件就是，根据统计的每段连续的数量可以求出每个字符的特殊序列出现的次数为 special_count =  [sum(max(0, x - k + 1) for x in value_list)  for _, value_list in cnt.items()]
然后对于每个字符，找出最大的 MAX(special_count),满足大于等于3次即为条件；

则可以找出k的左右边界
left = 1
right = n - 2

'''



from collections import defaultdict


def maximumLength(s: str) -> int:
    cnt = defaultdict(list)
    n = len(s)
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        cnt[s[i]].append(j - i)
        i = j

    left = 1
    right = n - 2
    while left <= right:
        mid = (left + right) // 2
        if max([sum(max(0, x - mid + 1) for x in value_list)  for _, value_list in cnt.items()]) >= 3:
            left = mid + 1
        else:
            right = mid - 1
    if right == 0:
        return - 1
    return right

s = 'abcaba'
s = 'aaaa'
s = 'abcdef'
print(maximumLength(s))
        
