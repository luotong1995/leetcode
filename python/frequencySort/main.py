'''
给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。一个字符出现的 频率 是它出现在字符串中的次数。

返回 已排序的字符串 。如果有多个答案，返回其中任何一个

输入: s = "tree"
输出: "eert"
解释: 'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。


输入: s = "cccaaa"
输出: "cccaaa"
解释: 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。

'''
import heapq


def frequencySort(s: str) -> str:
    f = {}
    for item in s:
        if item not in f:
            f[item] = 1
        else:
            f[item] += 1
    l = [(value, key) for key, value in f.items()]
    l.sort()
    l.reverse()
    r = ''
    for item in l:
        r += item[0] * item[1]
    return r


# 使用最大堆来实现，使用heapq来实现堆
def frequencySort2(s: str) -> str:
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    l = [(-value, key) for key, value in count.items()]
    heapq.heapify(l)
    res = ""
    while l:
        val, key = heapq.heappop(l)
        res += key * (-val)
    return res


if __name__ == '__main__':
    # print(frequencySort('ccaaa'))
    print(frequencySort2('ccaaa'))

    l = [3, 5, 7, 2, -1, 0]
    r = []
    heapq.heapify(l)
    while l:
        val = heapq.heappop(l)
        r.append(val)
    print(r)
