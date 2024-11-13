'''


给你两个长度相同的字符串，s 和 t。

将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

 

示例 1：

输入：s = "abcd", t = "bcdf", maxCost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
示例 2：

输入：s = "abcd", t = "cdef", maxCost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
示例 3：

输入：s = "abcd", t = "acde", maxCost = 0
输出：1
解释：a -> a, cost = 0，字符串未发生变化，所以最大长度为 1。
 

提示：

1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s 和 t 都只含小写英文字母。

思考：
这个题目做转换的时候是一个cost，看起来是每个下标对应的转换。然后这里是要求在maxCost这个 CONSTRAINTs 之内，找到最大的子字符串的长度。
这里可以用变长滑动窗口来实现，如果cost > maxCost 了，就需要移动 LEFT 边界。
1. left =0
2. right = 0 ~ n-1
3. 需要移动left的条件就是当前cost> maxCost的情况，cost = sum(abs(ord(s[i]) - ord(t[i])))
4. 更新maxLength = max(maxLength, right - left + 1)

'''
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    left = 0
    ans = 0
    cost = 0
    for right in range(len(s)):
        while cost + abs(ord(s[right]) - ord(t[right])) > maxCost:
            cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1
        cost += abs(ord(s[right]) - ord(t[right]))
        ans = max(ans, right - left + 1)
    return ans

print(equalSubstring("abcd", "cdef", 3))
print(equalSubstring("abcd", "acde", 0))
print(equalSubstring("abcd", "bcdf", 3))