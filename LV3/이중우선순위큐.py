import sys
import heapq
from collections import deque

def heapsort(iterable):
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

def solution(operations):
    arr = []
    answer = []
    
    for i in operations:
        if "I" in i:
            arr.append(int(i.split()[1]))
        arr = deque(heapsort((arr)))
        if len(arr) != 0:
            if i == "D -1":
                arr.popleft()
            elif i == "D 1":
                arr.pop()
    
    if len(arr) == 0:
        answer = [0,0]
    else:
        answer = [arr[-1], arr[0]]
        
    return answer