def solution(progresses, speeds):
    q = []
    answer = []
    
    for i in range(len(progresses)):
        days = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            days += 1
        q.append(days)

    while q:
        i = 1
        numberOfFun = 0
        if len(q) >= 2:
            if q[i-1] >= q[i]:
                temp = q[i-1]
                while q and q[i-1] <= temp:
                    q.pop(0)
                    numberOfFun += 1
            else:
                q.pop(0)
                numberOfFun += 1
        else:
            q.pop(0)
            numberOfFun += 1
        answer.append(numberOfFun)
        
    return answer