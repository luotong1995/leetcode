from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    a_dict = {}
    for item in arr:
        a_dict[item] = a_dict.get(item, 0) + 1

    return len(set(a_dict.values())) == len(a_dict)


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
