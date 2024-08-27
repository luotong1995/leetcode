from typing import List


# 总体积-柱子体积
def trap(height: List[int]) -> int:
    b = sum(height)
    size = len(height)
    l, r = 0, size - 1
    high = 1
    v = 0
    while l <= r:
        while l <= r and height[l] < high:
            l += 1
        while l <= r and height[r] < high:
            r -= 1
        v += r - l + 1
        high += 1
    return v - b


# 单调栈的方法，维护一个递减的单调栈，当前值大于栈顶元素，则pop，然后当栈里面有超过两个元素的时候，计算面积
def tarp2(height: List[int]) -> int:
    res = 0
    stack = list()
    n = len(height)

    for i in range(n):
        h = height[i]
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            left = stack[-1]
            l = i - left - 1
            c_h = min(height[left], height[i]) - height[top]
            res += l * c_h
        stack.append(i)
    return res

print(tarp2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
