def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer_sum = 0
    for i in range(len(A)):
        answer_sum += A[i] * B[i]
        
    return answer_sum 
