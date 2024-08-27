from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    import functools
    @functools.lru_cache()
    def back_track(s1):
        if not s1:
            return True

        res = False
        for i in range(1, len(s1) + 1):
            if s1[:i] in wordDict:
                res = back_track(s1[i:]) or res
        return res

    return back_track(s)


def wordBreak2(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * n
    dp[0] = True
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i] and s[i:j] in wordDict:
                dp[j] = True
    return dp[-1]


print(wordBreak('leetcode', ['leet', 'code']))
