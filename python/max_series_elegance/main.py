from typing import List
import itertools


def findMaximumElegance(items: List[List[int]], k: int) -> int:
    def compute_elegance_score(item):
        total_profit = sum([i[0] for i in item])
        distinct_categories = len(set([i[1] for i in item])) ** 2
        return total_profit + distinct_categories

    scores = []
    for item in list(itertools.combinations(items, k)):
        scores.append(compute_elegance_score(item))
    return max(scores)


def findMaximumElegance(items: List[List[int]], k: int) -> int:
    def compute_elegance_score(item):
        total_profit = sum([i[0] for i in item])
        distinct_categories = len(set([i[1] for i in item])) ** 2
        return total_profit + distinct_categories

    def find_subsequences(lst, k):
        def _find_subsequences(start, curr):
            if len(curr) == k:
                result.append(curr[:])
                return
            for i in range(start, len(lst)):
                curr.append(lst[i])
                _find_subsequences(i + 1, curr)
                curr.pop()

        result = []
        _find_subsequences(0, [])
        return result

    scores = []
    for item in find_subsequences(items , k):
        scores.append(compute_elegance_score(item))
    return max(scores)


# 示例
lst = [1, 2, 3, 4]
k = 3
subsequences = find_subsequences(lst, k)
print(subsequences)

if __name__ == '__main__':
    print(findMaximumElegance([[3, 2], [5, 1], [10, 1]], 2))
    items = [[3, 2], [5, 1], [10, 1]]
