# 문제 2. 점수의 총합에서 최고 점수와 최저 점수를 뺄셈하는 함수의 빈 칸 채우기
# 리듬체조 선수 영심은 지난 1년간 대회에 참가한 기록을 정리 중입니다. 
# 각 대회에서 받은 점수가 들어있는 리스트가 주어졌을 때, 
# 이 선수의 최고 점수와 최저 점수를 제외한 나머지 점수들의 합계를 구하려 합니다. 
# 이를 위해 다음의 단계로 프로그램 구조를 작성했습니다.
# 1. 모든 점수의 합을 구합니다.
# 2. 최고 점수와 최저 점수를 구합니다.
# 3. (모든 점수의 합) - (최고 점수) - (최저 점수) 의 값을 return 합니다.
# 대회별 점수가 들어있는 리스트 scores가 매개변수로 주어질 때, 
# 영심의 대회별 점수에서 최고 점수와 최저 점수를 제외한 나머지 점수의 합을 
# return 하도록 solution 함수를 작성하려 합니다. 
# 위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸을 알맞게 채워주세요.

# 코드
def func_a(s):
    ______
    return s[len(s)-1], s[0]

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def solution(scores):
    sum = func_______
    max, min = func_______
    return sum - max - min

# 실행
scores = [10,20,50,90,30,40]
ret = solution(scores)
print(ret)

# test
print(scores)
total = func_b(scores)
ma, mi = func_a(scores)
print( total , ma , mi)
print( total - ma - mi)

