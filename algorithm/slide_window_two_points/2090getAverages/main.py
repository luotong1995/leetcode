from typing import List


def getAverages(nums: List[int], k: int) -> List[int]:
    ans = []
    n = len(nums)
    c_sum = 0
    for i in range(n):
        if i + k >= n:
            ans.append(-1)
            continue
        
        if i < k:
            c_sum += sum(nums[i*2:i*2+2])
            ans.append(-1)
            continue
        
        c_sum += nums[i + k]
        ans.append(c_sum//(2*k+1))
        c_sum = c_sum - nums[i-k]
    return ans

def getAverages2(nums: List[int], k: int) -> List[int]:
    
    n = len(nums)
    ans = [-1] * n
    c_sum = 0
    for i in range(n):
        c_sum += nums[i]
        if i < 2*k:
            continue
        ans[i-k] = c_sum //(2*k + 1)
        c_sum -= nums[i - 2*k]
    return ans

nums = [7,4,3,9,1,8,5,2,6]
k = 3 
print(getAverages2(nums, k))
        
    


