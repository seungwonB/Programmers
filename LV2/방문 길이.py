def solution(dirs):
    dirs_dic = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
    stack = set()
    y, x = 0, 0
    cur_y, cur_x = 0, 0
    for i in dirs:
        next_y = cur_y + dirs_dic[i][0]
        next_x = cur_x + dirs_dic[i][1]
        
        if next_y >= -5 and next_y <= 5 and next_x >= -5 and next_x <= 5:
            # 출발지점, 도착지점을 모두 저장. 겹치는 길 set
            stack.add((cur_y, cur_x, next_y, next_x))
            stack.add((next_y, next_x, cur_y, cur_x))
            cur_y, cur_x = next_y, next_x

    return len(stack)//2