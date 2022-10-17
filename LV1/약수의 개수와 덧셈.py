def solution(left, right):
    answer = 0
    num_list = []
    cnt = 0
    
    for i in range(left, right+1):
        num_list.append(i)
    
    for i in range(len(num_list)):
        for j in range(1, num_list[i] + 1):
            if num_list[i] % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += num_list[i]
        else:
            answer -= num_list[i]
            
        cnt = 0
        
    return answer