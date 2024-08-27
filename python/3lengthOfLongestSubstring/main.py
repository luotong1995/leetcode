def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    j = 0
    re = 0
    n = len(s)
    a = set()
    while i < n and j < n:
        if s[j] not in a:
            a.add(s[j])
            re = max(re, j - i + 1)
            j += 1
        else:
            a.remove(s[i])
            i += 1
    return re


print(lengthOfLongestSubstring('abca'))
