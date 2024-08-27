def gcdOfStrings(str1: str, str2: str) -> str:
    def gcd(a: int, b: int) -> int:
        return a if b == 0 else gcd(b, a % b)

    # 两个字符串要么没有最大公因子，要么有最大公因子的长度就是字符串长度的最大公约数
    if str1 + str2 != str2 + str1: return ""
    return str1[0:gcd(len(str1), len(str2))]


print(gcdOfStrings('abcabcabc', 'abc'))
