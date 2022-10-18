def solution(s):
    answer = []
    temp = strAns = ''
    i = 0
    
    while (i<len(s)):
        if s[i] == " ":
            i += 1
        else:
            try:
                while(s[i] != " "):
                    temp += s[i]
                    i += 1
            except:
                pass
    
            answer.append(int(temp))
            temp = ''
    
    answer.sort()
    strAns += str(answer[0]) + " " + str(answer[-1])

    return strAns
    # split 쓰는 방법도 있음