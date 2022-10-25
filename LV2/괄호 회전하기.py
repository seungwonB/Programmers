def rotation(s):
    flag = True
    stack = []

    for i in s:
        if i == "[" or i == "(" or i == "{":
            stack.append(i)
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
        elif i == "}":
            if len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            else:
                flag = False

    if flag and len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        if rotation(s):
            answer += 1
        s = s[1:] + s[0]
        
    return answer