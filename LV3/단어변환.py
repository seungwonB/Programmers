from collections import deque

def check_diff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    
    if count == 1: return True
    else: return False

def solution(begin, target, words):
    if target not in words:
        return 0    
    
    q = deque()
    q.append([begin, 0])
    
    while q:
        word, count = q.popleft()
        
        if word == target: 
            return count
        
        for i in range(len(words)):
            temp = words[i]
            if(check_diff(word, temp)):
                q.append([temp, count+1])
    
    return 0