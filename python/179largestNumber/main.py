from typing import List


def largestNumber(nums: List[int]) -> str:
    if all([item == 0 for item in nums]):
        return '0'
    from functools import cmp_to_key
    str_list = []
    for item in nums:
        str_list.append(str(item))

    def compare(a, b):
        c = a + b
        d = b + a
        if c > d:
            return 1
        elif c == d:
            return 0
        else:
            return -1

    str_list.sort(key=cmp_to_key(compare), reverse=True)

    return ''.join(str_list)


print(largestNumber([10, 2]))
