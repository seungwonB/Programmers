def sort_numbers(numbers):
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i-1] > numbers[j]:
                temp = numbers[i - 1]
                numbers[i - 1] = numbers[j]
                numbers[j] = temp

def solution(numbers):
    ans_sum = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum1 = numbers[i] + numbers[j]
            if sum1 not in ans_sum:
                ans_sum.append(sum1)
            else:
                continue
    sort_numbers(ans_sum)

    return ans_sum