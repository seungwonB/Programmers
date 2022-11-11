def BFS(start, visited, computers):
    q = []
    q.append(start)
    visited[start] = 1

    while q:
        v = q.pop()

        for i in range(len(computers[0])):
            if computers[v][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)

def solution(n, computers):
    connected = 0
    visited = [0] * len(computers[0])

    for i in range(len(computers[0])):
        for j in range(len(computers[0])):
            if visited[j] == 0 and computers[i][j] == 1:
                BFS(i, visited, computers)
                connected += 1
                
    return connected