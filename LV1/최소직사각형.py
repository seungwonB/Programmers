def solution(sizes):
    arr_max = []
    arr_min = []
    
    for i in sizes:
        arr_max.append(max(i))
        arr_min.append(min(i))
    
    answer = max(arr_max) * max(arr_min)
    
    return answer