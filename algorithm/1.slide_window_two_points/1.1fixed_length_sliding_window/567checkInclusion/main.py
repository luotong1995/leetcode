'''
567.字符串的排列
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。


示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").

示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false
 

提示：

1 <= s1.length, s2.length <= 10^4
s1 和 s2 仅包含小写字母


思考：
题目是要看在s2中是否包含s1的排列，其实就是要看s2的子串是否包含s1的排列。
这里看到排列，如果单纯的直接求排列，时间复杂度肯定会超过题目的要求。
所以可以直接统计字母出现的个数是否一样，如果一样则满足情况。
1. 统计s1的长度n，s2的长度m，先统计s1中各个字母的个数
2. 统计s2中前n个字母的个数，如果一样则返回True
3. 从n开始，每次滑动窗口，新增一个删除一个，统计窗口中的字母个数，如果一样则返回True





'''


def checkInclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)
    if n > m:
        return False
    
    s1_cnt = [0] * 26
    s2_cnt = [0] * 26

    for i in range(n):
        s1_cnt[ord(s1[i]) - ord('a')] += 1
        s2_cnt[ord(s2[i]) - ord('a')] += 1
    
    if s1_cnt == s2_cnt:
        return True
    
    for i in range(n, m):
        s2_cnt[ord(s2[i]) - ord('a')] += 1
        s2_cnt[ord(s2[i - n]) - ord('a')] -= 1
        if s1_cnt == s2_cnt:
            return True
    return False


print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaooo"))
        