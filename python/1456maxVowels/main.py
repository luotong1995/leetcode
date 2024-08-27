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


# 滑动窗口
def maxVowels2(s: str, k: int) -> int:
    res = 0
    for i in range(k):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            res += 1
    if res == k:
        return res

    max_v = 0
    a = 0
    for i in range(len(s)):
        # 1进入窗口，更新统计量
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            a += 1
        if i < k - 1:
            continue
        # 2更新答案
        max_v = max(max_v, a)
        # 3下标为i-k+1的出窗口，更新统计量
        if s[i - k + 1] in ['a', 'e', 'i', 'o', 'u']:
            a -= 1
    return max_v


print(maxVowels2('abciiidef', 3))
