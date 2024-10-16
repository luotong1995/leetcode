'''
1146 快照数组

实现支持下列接口的「快照数组」- SnapshotArray：

SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
void set(index, val) - 会将指定索引 index 处的元素设置为 val。
int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
 

示例：

输入：["SnapshotArray","set","snap","set","get"]
     [[3],[0,5],[],[0,6],[0,0]]
输出：[null,null,0,null,5]
解释：
SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
snapshotArr.set(0,5);  // 令 array[0] = 5
snapshotArr.snap();  // 获取快照，返回 snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
 

提示：

1 <= length <= 50000
题目最多进行50000 次set，snap，和 get的调用 。
0 <= index < length
0 <= snap_id < 我们调用 snap() 的总次数
0 <= val <= 10^9


思考：
使用一个dict来存储每个index的变化，用[snap_id, value]存储这个变化
set: 直接在dict中append  [snap_id, value]的数据
get: 根据index，获取每个index下面的数据变化，然后使用二分查找找到对应的snap_id对应的下标，然后找到value即为返回值，使用lower_bound找到最后一个大于等于snap_id的下标

'''

from bisect import bisect_left, bisect_right
from collections import defaultdict


class SnapshotArray:

    def __init__(self, length: int):
        self.cur_snap_id = 0
        self.data = defaultdict(list)


    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.cur_snap_id, val))


    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id -1


    def get(self, index: int, snap_id: int) -> int:
        snap_data = self.data[index]
        final_index = bisect_left(snap_data, (snap_id + 1,)) - 1
        return self.data[index][final_index][1] if final_index >= 0 else 0
        

["SnapshotArray","set","set","snap","snap","get","get","snap"]
[[1],[0,1],[0,2],[],[],[0,0],[0,0],[]]

["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]

# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(1)
print(obj.set(0,1))
print(obj.set(0,2))
print(obj.snap())
print(obj.snap())
print(obj.get(0,0))
print(obj.get(0,0))
print(obj.snap())

obj = SnapshotArray(3)
print(obj.set(0,5))
print(obj.snap())
print(obj.set(0,6))
print(obj.get(0,0))