from collections import defaultdict
def solution(k, room_number):
    answer = []
    rdict = defaultdict()
    for num in room_number:
        idx = num
        visit = {idx}			# 배정 가능한 방을 찾기 까지의 방문기록
        while idx in rdict:		# idx가 dictionary에 없을 때 까지 반복
            idx = rdict[idx]
            visit.add(idx)
        for room in visit:		# 방문했던 방들에 다음으로 배정가능한 번호를 저장
            rdict[room] = idx+1
        answer.append(idx)
    return answer