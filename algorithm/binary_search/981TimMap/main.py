'''
基于时间的键值存储

设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。

实现 TimeMap 类：

TimeMap() 初始化数据结构对象
void set(String key, String value, int timestamp) 存储给定时间戳 timestamp 时的键 key 和值 value。
String get(String key, int timestamp) 返回一个值，该值在之前调用了 set，其中 timestamp_prev <= timestamp 。如果有多个这样的值，它将返回与最大  timestamp_prev 关联的值。如果没有值，则返回空字符串（""）。
 
示例 1：

输入：
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
输出：
[null, null, "bar", "bar", null, "bar2", "bar2"]

解释：
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1   
timeMap.get("foo", 1);         // 返回 "bar"
timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4  
timeMap.get("foo", 4);         // 返回 "bar2"
timeMap.get("foo", 5);         // 返回 "bar2"


提示：

1 <= key.length, value.length <= 100
key 和 value 由小写英文字母和数字组成
1 <= timestamp <= 107
set 操作中的时间戳 timestamp 都是严格递增的
最多调用 set 和 get 操作 2 * 105 次


思考：
让value_dict存储数据，timestamp存储时间
value_dict = {'foo': ['bar', 'bar2']}
timestamp_dict ={'foo': [1, 4]}

set: 直接在value_dict和timestamp_dict后面增加数据
get: 从timestamp_dict中找出最后一个大于等于timestamp的值，可以使用lower_bound(timestamp + 1) - 1或者使用upper_bound - 1,找出第一个大于目标的位置然后-1
但是如果找不到，index为-1，则直接返回""


'''
from bisect import bisect_right
from collections  import defaultdict

class TimeMap:

    def __init__(self):
        self.value_dict = defaultdict(list)
        self.timestamp_dict = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_dict[key].append(value)
        self.timestamp_dict[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.timestamp_dict[key]
        pos = bisect_right(timestamps, timestamp) - 1
        if pos < 0:
            return ""
        return self.value_dict[key][pos]


["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

obj = TimeMap()
print(obj.set('love','high',10))
print(obj.set('love','low',20))
print(obj.get('love',5))
print(obj.get('love',10))
print(obj.get('love',15))
print(obj.get('love',20))
print(obj.get('love',25))
