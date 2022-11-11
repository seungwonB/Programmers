def solution(food):
    answer = ''
    
    for i in range(len(food)):
        if food[i] == 1:
            continue
        temp = int(food[i]/2)
        for j in range(temp):
            answer += str(i)
    
    answer += "0" + answer[::-1]
    return answer