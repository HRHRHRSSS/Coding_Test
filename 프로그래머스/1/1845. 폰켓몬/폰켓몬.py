from collections import defaultdict

def solution(nums):
    nums_map = defaultdict(int)
    
    for i in nums:
        nums_map[i] += 1
    
    k = len(nums)//2
    
    if len(nums_map) >= k:
        return k
    else:
        return len(nums_map)