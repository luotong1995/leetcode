'''
1888. 使二进制字符串字符交替的最少反转次数
给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次：

类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。
请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。

我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。

比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。
 

示例 1：

输入：s = "111000"
输出：2
解释：执行第一种操作两次，得到 s = "100011" 。
然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
示例 2：

输入：s = "010"
输出：0
解释：字符串已经是交替的。
示例 3：

输入：s = "1110"
输出：1
解释：对第二个字符执行第二种操作，得到 s = "1010" 。
 

提示：

1 <= s.length <= 10^5
s[i] 要么是 '0' ，要么是 '1' 。

思考：
类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
类型1的逻辑是删除最左边的字符，加载最右边；这个操作其实就是把字符串拼接到一起，然后进行滑动窗口；
类型 2的操作是求翻转的次数；
最终得到的字符串只有两种情况，010101和101010；如何判断这两种情况翻转的次数书多少；
直接与原字符串进行对比，如果元素不相等，则需要进行翻转，即可统计翻转的次数；

直接对于两种情况都进行字符串的扩充，这样可以不用考虑数组index对应的问题。

'''

def minFlips(s: str) -> int:

    n = len(s)
    ans = 0 
    p1 = ''.join(['1' if i%2==0 else '0' for i in range(2*n)])
    p2 = ''.join(['0' if i%2==0 else '1' for i in range(2*n)])

    a1 = sum([1 if p1[i]!= s[i] else 0 for i in range(n)])
    a2 = sum([1 if p2[i]!= s[i] else 0 for i in range(n)])
    ans = min(a1, a2)

    s1 = s + s

     # 滑动窗口更新反转计数
    for i in range(1, n):
        # 移除左侧字符对 diff1 和 diff2 的影响
        if s1[i - 1] != p1[i - 1]:
            a1 -= 1
        if s1[i - 1] != p2[i - 1]:
            a2 -= 1
        
        # 添加右侧字符对 diff1 和 diff2 的影响
        if s1[i + n - 1] != p1[i + n - 1]:
            a1 += 1
        if s1[i + n - 1] != p2[i + n - 1]:
            a2 += 1
        
        # 更新最小反转次数
        ans = min(ans, a1, a2)
    
    return ans


# print(minFlips("111000"))
# print(minFlips("010"))
# print(minFlips("1110"))
print(minFlips('01001001101'))


# 01001001101
# 0100 1001101
#   10101010101
# 0100100110101