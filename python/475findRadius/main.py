from typing import List


# 对于每一个房间，在加热器中选择距离最近的加热器。得到的结果是对于每一个房间都有一个最近的加热半径，选取最大的加热半径
def findRadius(houses: List[int], heaters: List[int]) -> int:
    res = 0
    heaters = sorted(heaters)
    for item in houses:
        # cur_dis = findMin(heaters, item)
        i = binarySearch(heaters, item)
        j = i + 1
        l_dis = float('inf') if i < 0 else item - heaters[i]
        r_dis = float('inf') if j > len(heaters) - 1 else heaters[j] - item
        cur_dis = min(l_dis, r_dis)
        if cur_dis > res:
            res = cur_dis
    return res


def findMin(heaters, target):
    min = float('inf')
    for item in heaters:
        if abs(item - target) < min:
            min = abs(item - target)
    return min


## binary search
def binarySearch(nums, target):
    i = 0
    j = len(nums) - 1
    if nums[i] > target:
        return -1
    while i < j:
        mid = (j - i + 1) // 2 + i
        if nums[mid] > target:
            j = mid - 1
        else:
            i = mid
    return i

## 找到第一个大于house的发热器，然后找到最小的半径
def findRadius2(houses: List[int], heaters: List[int]) -> int:
    n = len(heaters)
    houses.sort()
    heaters.sort()
    j = 0
    max_radius = 0
    for house in houses:
        while j < n and heaters[j] <= house:
            j += 1
        # now heaters[j - 1] <= house < heaters[j]
        if j == 0:
            radius = heaters[j] - house
        elif j == n:
            radius = house - heaters[j - 1]
        else:
            radius = min(heaters[j] - house, house - heaters[j - 1])
        max_radius = max(radius, max_radius)
    return max_radius


# print(binarySearch([1, 2, 3], 2))

print(findRadius2([1, 2, 3], [2]))
print(findRadius2([1, 2, 3, 4], [4, 1]))
print(findRadius2([1, 5], [2]))
