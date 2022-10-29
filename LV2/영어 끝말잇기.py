def solution(n, words):
    stack = []
    temp = 0
    answer = []
    
    for idx, i in enumerate(words):
        if len(stack) == 0:
            stack.append(i)
        elif i not in stack and stack[-1][-1] == i[0]:
            stack.append(i)
        else:
            temp = idx
            break
    print(temp)
    if temp == 0:
        answer = [0, 0]
    else:
        answer = [temp%n+1, temp//n+1]
        # if (idx + 1) % n == 0:
        #     answer.append(n)
        # else:
        #     answer.append((idx + 1) % n)
        # answer.append(temp//n+1)
    return answer


    # for p in range(1, len(words)):
    #     if words[p][0] != words[p-1][-1] or 
    #         words[p] in words[:p]: 
    #             return [(p%n)+1, (p//n)+1]
    # else:
    #     return [0,0]
