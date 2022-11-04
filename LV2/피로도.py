from itertools import permutations

def solution(k, dungeons):
    
    permu = list(permutations(dungeons, len(dungeons)))
    arr = []
    
    for i in permu:
        temp = k
        answer = 0
        for j in i:
            if temp >= j[0]:
                temp -= j[1]
                answer += 1
        arr.append(answer)
        
    return max(arr)