from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
        
    for end in graph.keys():
        graph[end].sort(reverse=True)
        
    stack = ["ICN"]
    path = []
    
    while stack:
        temp = stack.pop();
        
        if temp not in graph or not graph[temp]:
            path.append(temp)
        else:
            stack.append(temp)
            stack.append(graph[temp].pop())
    
    return path[::-1]