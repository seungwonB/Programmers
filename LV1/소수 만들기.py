from itertools import *

def solution(nums):
    combinums = list(combinations(nums, 3))
    sumArr = [sum(i) for i in combinums]
    non_sosu = []
    
    for i in sumArr:
        for j in range(2, i):
            if i % j == 0:
                non_sosu.append(i)
                break
    answer = 0
    for i in sumArr:
        if i not in non_sosu:
            answer += 1
    
    return answer

    # answer = 0
    # for i in combinations(nums, 3):
    #     sumArr = sum(i)
    #     for j in range(2, sumArr):
    #         if sumArr % j == 0:
    #             break
    #     else:
    #         answer += 1
    # return answer