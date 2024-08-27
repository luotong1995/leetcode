from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break
    return result


# 单调栈
def dailyTemperatures2(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        if len(stack) == 0:
            stack.append(i)
        else:
            while stack and temperatures[i] > temperatures[stack[-1]]:
                cur_index = stack[-1]
                stack.pop()
                result[cur_index] = i - cur_index
            stack.append(i)
    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures([30, 40, 50, 60]))
print(dailyTemperatures([30, 60, 90]))

print(dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures2([30, 40, 50, 60]))
print(dailyTemperatures2([30, 60, 90]))
