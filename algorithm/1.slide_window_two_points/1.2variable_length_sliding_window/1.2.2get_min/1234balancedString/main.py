'''
有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。

假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。

 

给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。

你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。

请返回待替换子串的最小可能长度。

如果原字符串自身就是一个平衡字符串，则返回 0。

 

示例 1：

输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。
示例 2：

输入：s = "QQWE"
输出：1
解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
示例 3：

输入：s = "QQQW"
输出：2
解释：我们可以把前面的 "QQ" 替换成 "ER"。 
示例 4：

输入：s = "QQQQ"
输出：3
解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
 

提示：

1 <= s.length <= 10^5
s.length 是 4 的倍数
s 中只含有 'Q', 'W', 'E', 'R' 四种字符


思考：
判断是否是平衡字符串，需要统计每个字符的个数，然后判断是否都是n/4，如果是，则返回0。
这里题目中要求最小长度的平衡子串，需要用到滑动窗口，滑动窗口的长度是不固定的，所以需要用到双指针，一个指向窗口的左边界，一个指向窗口的右边界。

求最小，使用滑动窗口的时候，每次固定right，然后求出当前right下的最小平衡子字符串，然后再求出全局最小的平衡子字符串。

1. 统计字符串中每个字符出现的次数
2. 求出判断平衡的target的数量
3. 判断是否是平衡字符串，如果是直接返回0
4. 迭代right指针，然后表示滑动窗口进入了一个字符，所以得count[ch] -= 1
5. 循环判断left指针，如果字符串中剩余字符数量都小于等于target，窗口外的字符满足平衡条件，那么就可以更新res的值，此时res = min(res, right - left + 1)等于，表示窗口内的字符是当前right条件下的满足条件的字符串，然后通过不断右边移动left，缩短窗口，找到最小的长度


灵神答案：
根据题意，如果在待替换子串之外的任意字符的出现次数超过 m= n/4 ，那么无论怎么替换，都无法使这个字符在整个字符串中的出现次数为 m。
反过来说，如果在待替换子串之外的任意字符的出现次数都不超过 m，那么可以通过替换，使 s 为平衡字符串，即每个字符的出现次数均为 m。
对于本题，设子串的左右端点为 left 和 right，枚举 right，如果子串外的任意字符的出现次数都不超过 m，则说明从 left 到 right 的这段子串可以是待替换子串，
用其长度 right−left+1 更新答案的最小值，并向右移动 left，缩小子串长度。
'''



from typing import Counter


def balancedString(s: str) -> int:
    n = len(s)
    target = n // 4
    count = Counter(s)
    if all(count[ch] == target for ch in 'QWER'):
        return 0
    left = 0
    res = n
    for right, ch in enumerate(s):
        count[ch] -= 1
        while left < n and all(count[ch] <= target for ch in 'QWER'):
            res = min(res, right - left + 1)
            count[s[left]] += 1
            left += 1

    return res


# print(balancedString("QQQQ"))
print(balancedString("QQQW"))
print(balancedString("QQWE"))
print(balancedString("QWER"))
print(balancedString("QWERQQ"))
        