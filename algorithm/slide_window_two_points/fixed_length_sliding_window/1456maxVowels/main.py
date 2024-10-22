'''
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。

 

示例 1：

输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
示例 2：

输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
示例 3：

输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
示例 4：

输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
示例 5：

输入：s = "tryhard", k = 4
输出：1
 

提示：

1 <= s.length <= 10^5
s 由小写英文字母组成
1 <= k <= s.length
'''



# 暴力求解
def maxVowels(s: str, k: int) -> int:
    max_v = 0
    for i in range(len(s) - k + 1):
        a = s[i:i + k]
        max_v = max(count_vowels(a), max_v)
        if max_v == k:
            return max_v
    return max_v


def count_vowels(s):
    count = 0
    for item in s:
        if item in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


# 定长滑动窗口
def maxVowels2(s: str, k: int) -> int:
    i = 0
    ans = 0
    c_num = 0
    n = len(s)
    for i in range(n):
        if s[i] in 'aeiouAEIOU':
            c_num += 1
        
        if i < k - 1:
            continue
        ans = max(ans, c_num)
        if s[i-k+1] in 'aeiouAEIOU':
            c_num -= 1
    return ans


print(maxVowels2('abciiidef', 3))
print(maxVowels2('abcdef', 3))
