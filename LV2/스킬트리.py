def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        stack = ''
        for j in i:    
            if j in skill:
                stack += j
        
        # if skill.startswith(stack):
        if stack == skill[0:len(stack)]:
            answer += 1
        
    return answer