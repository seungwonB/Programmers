def solution(s):
    flag = True
    stack_s = []

    for i in range(len(s)):
        if (s[i] == '('):
            stack_s.append(s[i])
        else:
            if(len(stack_s) != 0):
                stack_s.pop()
            else:
                flag = False
                
    if flag and len(stack_s) == 0:
        return True
    else:
        return False