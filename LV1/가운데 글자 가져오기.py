def solution(s):
    half_len = int(len(s)//2)
    
    if (len(s) % 2 == 0):
        answer = s[half_len - 1 : half_len + 1]
    else:
        answer = s[half_len]

    return answer

    # return str[(len(str)-1)//2:len(str)//2+1]
