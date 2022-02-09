# 문제 8. 평균과 가장 큰 차이가 나는 점수 구하는 함수 수정하기
# A 반의 담임선생님은 최근에 치른 수학 시험을 결과를 분석하려고 합니다. 
# 평균 점수를 구한 후 평균 점수와 가장 큰 차이가 나는 점수가 몇 점인지를 알아보려고 합니다. 
# 예를 들어 5명의 학생 점수가 [ 10 90 50 30 60 ] 일 때 평균은 48점입니다. 
# 각 점수와 평균과의 차이는 아래와 같습니다.
# 학생별 점수   평균과의 차이
# 10            38
# 90            42
# 50            2
# 30            18
# 60            12
# 평균과 가장 큰 차이가 나는 학생 점수는 90점입니다. 
# 학생들의 점수를 저장한 리스트 scores 가 매개변수로 전달될 때 
# 평균과 가장 큰 차이가 나는 학생의 점수를 return 하도록 solution 함수를 작성했습니다. 
# 그러나 코드 일부분이 잘못되어 있어서 올바르게 동작하지 않습니다. 
# 주어진 코드에서 한 줄만 변경하여 모든 입력에 대해 올바르게 동작하도록 수정해주세요

# 코드
def func_a(a):
    total = 0
    for i in a:
        total += i
    return total

def func_b(a, b):
    return b if a < b else a

def func_c(a, b):
    max_diff = 0
    max_score = 0
    for i in b:
        diff = func_b(a, i)
        if max_diff > diff:
            max_diff = diff
            max_score = i
    return max_score

def solution(scores):
    total = func_a(scores)
    avg = total // len(scores)
    answer = func_c(avg, scores)
    return answer

# 실행
scores = [10, 90, 50, 30, 60]
ret = solution(scores)
print(ret)





