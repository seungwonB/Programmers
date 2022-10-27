def solution(numbers):
    # 문자열로 치환
    numbers = list(map(str, numbers))
    # 1000이하 이기 때문에 3자리 수, 첫 번째 문자열로 비교함
    # 내림차순으로 정렬
    numbers.sort(key=lambda x:x*3, reverse=True)
    # 000을 위해 int로 치환 후 다시 str로
    return str(int(''.join(numbers)))

    