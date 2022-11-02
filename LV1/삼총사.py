from itertools import combinations

def solution(number):
    count = 0
    comb = list(combinations(number, 3))
    
    for i in comb:
        answer = 0
        for j in i:
            answer += j
        if answer == 0:
            count += 1
            
    return count

   # cnt = 0
   #  for i in combinations(number,3) :
   #      if sum(i) == 0 :
   #          cnt += 1
   #  return cnt