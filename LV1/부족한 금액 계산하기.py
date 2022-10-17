def solution(price, money, count):
    ans_sum = 0
    for i in range(1, count+1):
        ans_sum += (price*i)
    if ans_sum - money < 0:
        return 0
    else:
        return ans_sum - money