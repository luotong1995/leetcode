'''
比较字符串最小字母出现频次

定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。

例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。

现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。

请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。

 

示例 1：

输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
示例 2：

输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
 

提示：

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j]、words[i][j] 都由小写英文字母组成

思考：
需要依次用query中的元素，去words中找到符合条件的元素，然后进行+1
1. 需要依次计算出query中和words中的f(s)的值是多少
2. [3,2], [1,2,3,4]
3. 二分查找，第一个大于x的下标,使用lower_bound(x+1)
'''
from typing import List

def f(x):
    x.sort()
    count = 1
    cur = x[0]
    for i in range(1, len(x)):
        if x[i] != cur:
            break
        count += 1
        
    return count

def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def numSmallerByFrequency(queries: List[str], words: List[str]) -> List[int]:
    query = [f(list(item)) for item in queries]
    word = [f(list(item)) for item in words]
    word.sort()
    n = len(word)
    ans = []
    for item in query:
        left_index = lower_bound(word, item + 1)
        if left_index != n:
            ans.append(n - left_index)
        else:
            ans.append(0)
    
    return ans

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
queries = ["cbd"]
words = ["zaaaz"]

queries = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
print(numSmallerByFrequency(queries, words))