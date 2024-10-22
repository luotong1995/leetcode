'''
2187 完成旅途的最少时间

给你一个数组 time ，其中 time[i] 表示第 i 辆公交车完成 一趟旅途 所需要花费的时间。

每辆公交车可以 连续 完成多趟旅途，也就是说，一辆公交车当前旅途完成后，可以 立马开始 下一趟旅途。每辆公交车 独立 运行，也就是说可以同时有多辆公交车在运行且互不影响。

给你一个整数 totalTrips ，表示所有公交车 总共 需要完成的旅途数目。请你返回完成 至少 totalTrips 趟旅途需要花费的 最少 时间。


示例 1：

输入：time = [1,2,3], totalTrips = 5
输出：3
解释：
- 时刻 t = 1 ，每辆公交车完成的旅途数分别为 [1,0,0] 。
  已完成的总旅途数为 1 + 0 + 0 = 1 。
- 时刻 t = 2 ，每辆公交车完成的旅途数分别为 [2,1,0] 。
  已完成的总旅途数为 2 + 1 + 0 = 3 。
- 时刻 t = 3 ，每辆公交车完成的旅途数分别为 [3,1,1] 。
  已完成的总旅途数为 3 + 1 + 1 = 5 。
所以总共完成至少 5 趟旅途的最少时间为 3 。
示例 2：

输入：time = [2], totalTrips = 1
输出：2
解释：
只有一辆公交车，它将在时刻 t = 2 完成第一趟旅途。
所以完成 1 趟旅途的最少时间为 2 。
 

提示：

1 <= time.length <= 105
1 <= time[i], totalTrips <= 107


思考：
求出最少的时间，满足次数总和大于等于totalTrips，首先可以看到，最差的情况也是最小的耗时*需要完成的总共的次数totalTrips，
所以右边边界为：min(time) * totalTrips
然后左边界为1，
使用二分查找的方式来从1 ～ min(time) * totalTrips，之间找出总共的旅途数第一个大于等于totalTrips的时间。


'''

from typing import List


def minimumTime(time: List[int], totalTrips: int) -> int:
    
    min_value = min(time)
    max_value =  min_value * totalTrips
    # nums = [i for i in range(1, max_value+1, 1)]

    left = 1
    right = max_value
    while left <= right:
        mid = left + (right - left) // 2
        cur_total = sum([(mid//item)  for item in time])
        if cur_total < totalTrips:
            left = mid + 1
        else:
            right = mid - 1
    return left

# time = [2]
# totalTrips = 1

# time = [1,2,3]
# totalTrips = 5

time = [5,10,10]
totalTrips = 9
print(minimumTime(time, totalTrips))