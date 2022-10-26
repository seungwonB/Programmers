def solution(participant, completion):
    dict_par = dict()
    for i in participant:
        dict_par[i] = 0
    
    for i in participant:
        dict_par[i] += 1
    
    for i in completion:
        dict_par[i] -= 1
        
    return [k for k, v in dict_par.items() if v == 1][0]
