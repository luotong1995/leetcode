'''
给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。


示例 1：

输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"
解释：letters 中字典上比 'a' 大的最小字符是 'c'。
示例 2:

输入: letters = ["c","f","j"], target = "c"
输出: "f"
解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。
示例 3:

输入: letters = ["x","x","y","y"], target = "z"
输出: "x"
解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。
 

提示：

2 <= letters.length <= 104
letters[i] 是一个小写字母
letters 按非递减顺序排序
letters 最少包含两个不同的字母
target 是一个小写字母


思考：
第一个大于target的下标：可以转换为`第一个大于等于 target+1 的下标` ，low_bound(target+1)
继续使用>=的方法来进行求解
'''


from typing import List


def nextGreatestLetter(letters: List[str], target: str) -> str:
    n = len(letters)
    left = 0
    right = n - 1
    target = chr(ord(target) + 1)
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == n:
        return letters[0]
    return letters[left]

letters = ["c","f","j"]
letters = ["x","x","y","y"]
target = "z"
print(nextGreatestLetter(letters, target))
        


