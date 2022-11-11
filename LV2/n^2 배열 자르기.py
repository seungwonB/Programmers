def solution(n, left, right):
    arr = []

    if left-n < 0:
        i = 0
    else:
        i = int(left/n)
        
    j = left % n

    while left != right+1:
        arr.append(max(i, j) + 1)
        left += 1

        if j == n-1:
            i += 1
            j = 0
        else:
            j += 1
            
    return arr
