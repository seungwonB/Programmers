def solution(people, limit):
    head = 0
    tail = len(people) - 1
    answer = 0
    people.sort()
    while(tail >= head):
        if people[head] + people[tail] > limit:
            tail -= 1
        else:
            head += 1
            tail -= 1
        answer += 1

    return answer