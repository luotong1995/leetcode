# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

def tribonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    a, b, c, r = 0, 1, 1, 1
    for i in range(3, n + 1):
        r = a + b + c
        a = b
        b = c
        c = r
    return r


print(tribonacci(25))
