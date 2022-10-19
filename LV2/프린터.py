from collections import deque

def solution(priorities, location):
    answer = 0
    doc = deque(priorities)
    temp = deque([x for x in range(len(doc))])
    
    while doc:
        p = doc.popleft()
        if doc:
            if p < max(doc):
                doc.append(p)
                temp.append(temp.popleft())
            else:
                answer += 1
                if temp[0] == location:
                    return answer
                else:
                    temp.popleft()
    
    return answer + 1