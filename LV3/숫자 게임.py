def solution(A, B):
    # 내림차순 정렬
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer = 0
    
    for i in A:
        # 순차적으로 A의 원소와 B의 첫 번째 원소 비교하여 
        # A의 원소가 더 크면 A의 다음 원소 비교
        if i >= B[0]: 
            continue
        # B의 첫 번째 원소가 더 크면 승점+1
        # 첫 번째 원소 삭제
        else:
            answer += 1
            del B[0]
    
    return answer