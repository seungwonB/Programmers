from collections import defaultdict

def solution(id_list, report, k):
    report = list(set(report))
    answer = []
    send_report = defaultdict(set)
    get_report = defaultdict(int)
    
    for i in report:
        send_user, get_user = i.split()
        send_report[send_user].add(get_user)
        get_report[get_user] += 1
    
    for i in id_list:
        result = 0
        for j in send_report[i]:
            if get_report[j] >= k:
                result += 1
        answer.append(result)
        
    return answer

# 0 배열 생성
answer = [0] * len(id_list)
# 신고 받은 횟수 배열
reports = {x : 0 for x in id_list}

for i in set(report):
    # 신고 받은 횟수 저장
    reports[i.split()[1]] += 1

print(reports)
for i in set(report):
    # 각 유저의 신고 받은 횟수가 k보다 크면
    if reports[i.split()[1]] >= k:
        # 신고한 유저의 자리를 찾아서 ++
        answer[id_list.index(i.split()[0])] += 1
