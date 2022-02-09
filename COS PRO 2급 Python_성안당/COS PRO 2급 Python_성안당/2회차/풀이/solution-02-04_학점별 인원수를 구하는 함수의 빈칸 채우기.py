# 문제 4. 학점별 인원 수를 구하는 함수의 빈 칸 채우기
# 열망 대학교에서는 다음과 같이 학생들의 점수에 따라 학점을 부여합니다.
# 85점 ~ 100점 : A 학점
# 70점 ~ 84점 : B 학점
# 55점 ~ 69점 : C 학점
# 40점 ~ 54점 : D 학점
# 0점 ~ 39점 : F 학점
# 학생들의 점수가 들어있는 리스트 scores가 매개변수로 주어질 때, 
# A 학점, B 학점, C 학점, D 학점, F 학점을 받은 학생들의 수를 리스트에 순서대로 담아 return 하도록 
# solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.


## 답안
def solution(scores):
    grade_counter = [ 0 for i in range(5) ]
    for i in scores:
        if i >= 85:
            grade_counter[0] += 1
        elif i >= 70:
            grade_counter[1] += 1
        elif i >= 55:
            grade_counter[2] += 1
        elif i >= 40:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter


## 비교해보기
# def solution(scores):
#     grade_counter = [ 0 for i in range(5) ]
#     for i in scores:
#         if i >= 40:
#             grade_counter[0] += 1
#         elif i >= 55:
#             grade_counter[1] += 1
#         elif i >= 70:
#             grade_counter[2] += 1
#         elif i >= 85:
#             grade_counter[3] += 1
#         else:
#             grade_counter[4] += 1
#     return grade_counter

scores = [10,20,30,40,50,60,70,80,90,100]
ret = solution(scores)
print(ret)

