def solution(ingredient):
    stack = []
    hamburger = 0

    for i in ingredient:
        stack.append(i)

        if len(stack) >= 4:
            if stack[-4:] == [1,2,3,1]:
                hamburger += 1
                for i in range(4):
                    stack.pop()
    
    return hamburger