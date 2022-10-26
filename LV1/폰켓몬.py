def solution(nums):
    n = int(len(nums)/2)
    nums = list(set(nums))
    
    if len(nums) > n:
        return n
    else:
        return len(nums)
    
    # return min(len(nums)/2, len(set(nums)))
    