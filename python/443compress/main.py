'''
给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。


示例 1：

输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
示例 2：

输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：唯一的组是“a”，它保持未压缩，因为它是一个字符。
示例 3：

输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
'''
from typing import List


def compress(chars: List[str]) -> int:
    ans = []
    count = 1
    if len(chars) == 0:
        return ans
    ans.append(chars[0])
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            count += 1
        else:
            if count > 1:
                res = []
                while count > 0:
                    res.append(str(count % 10))
                    count //= 10
                res.reverse()
                ans.extend(res)
            count = 1
            ans.append(chars[i])
    if count > 1:
        res = []
        while count > 0:
            res.append(str(count % 10))
            count //= 10
        res.reverse()
        ans.extend(res)
    for i, item in enumerate(ans):
        chars[i] = item
    while len(chars) > len(ans):
        chars.pop()
    return len(ans)


if __name__ == '__main__':
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    # chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(compress(chars))
    print(chars)
