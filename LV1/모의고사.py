import math

def OverNumArr(answers, arr):
    multiple_num = 1
    if len(answers) > len(arr):
        temp = len(answers) - len(arr)  # 6-5 = 1
        multiple_num = multiple_num + math.ceil(temp / len(arr))
    return multiple_num


def select_num(answers, arr):
    answer = 0
    mul_num = OverNumArr(answers, arr)
    arr = arr * mul_num
    for i in range(len(answers)):
        if answers[i] == arr[i]:
            answer += 1
    return answer

def solution(answers):
    arr_answer = []
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    n1 = select_num(answers, num_1)
    n2 = select_num(answers, num_2)
    n3 = select_num(answers, num_3)

    max_num = max(n1, n2, n3)
    num_arr = [n1, n2, n3]

    for i in range(3):
        if max_num == num_arr[i]:
            arr_answer.append(i + 1)

    return arr_answer