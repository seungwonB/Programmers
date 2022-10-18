def solution(brown, yellow):
    height = width = 0
    array = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            width = int(yellow/i)
            height = i
            
            if 2*(width+2) + (2*height) == brown:
                array.append(width+2)
                array.append(height+2)
                
    return array[:2]