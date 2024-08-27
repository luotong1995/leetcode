## 暴力求解法
def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s
    max = 0
    max_str = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]
            if (j - i + 1) > max and isPalindrome(temp) and len(temp) > max:
                max = len(temp)
                max_str = temp
    return max_str


def isPalindrome(s) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


## 动态规划
def longestPalindrome2(s: str) -> str:
    if len(s) < 2:
        return s
    max_l = 1
    start = 0
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for i in range(n):
        for j in range(i):
            if s[i] != s[j]:
                dp[j][i] = 0
            else:
                if i - j < 3:
                    dp[j][i] = 1
                else:
                    dp[j][i] = dp[j + 1][i - 1]
            if dp[j][i] and i - j + 1 > max_l:
                max_l = i - j + 1
                start = j

    return s[start: start + max_l]


print(longestPalindrome2('abade'))
