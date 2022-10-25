import re

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()

    # 2
    for id in new_id:
        if id.islower() or id.isdigit() or id in ['-', '_', '.']:
            answer += id
    new_id = answer
    
    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4
    if len(new_id) >= 1:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if len(new_id) >= 1:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    
    # 5
    if new_id == '':
        new_id = "a"
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    
    # 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    
    return new_id