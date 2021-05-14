#programmers: 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        a = -a if not s else a
        answer += a
    return answer

print(solution([1,2,3],[True,True,True]))
