from typing import List


def numRabbits(answers: List[int]) -> int:
    a_dict = {}
    result = 0
    for item in answers:
        a_dict[item] = a_dict.get(item, 0) + 1

    for k, v in a_dict.items():
        if k == 0:
            result += v
            continue
        if v < k + 1:
            result += k + 1
            continue

        if v % (k + 1):
            result += (v // (k + 1)) * (k + 1) + (k + 1)
        else:
            result += (v / (k + 1)) * (k + 1)
    return int(result)


def numRabbits2(answers: List[int]) -> int:
    a_dict = {}
    result = 0
    for i in range(len(answers)):
        if a_dict.get(answers[i], 0) == 0:
            result = result + answers[i] + 1
            a_dict[answers[i]] = answers[i]
        else:
            a_dict[answers[i]] = a_dict[answers[i]] - 1
    return int(result)


# print(numRabbits([1, 1, 2]))
print(numRabbits([0, 0, 1, 1, 1]))
print(numRabbits2([0, 0, 1, 1, 1]))
