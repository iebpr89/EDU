# 문제 6. 몸무게가 큰 사람의 수를 구하는 함수 수정하기
# 비만 문제가 이슈가 되어 안뚱 중학교에서는 비만 관리를 위해 학생들의 몸무게를 조사하였습니다. 
# 학생들의 몸무게가 들어있는 목록에서 몸무게가 k보다 큰 사람은 몇 명인지 구하려합니다. 
# 예를 들어 다음과 같은 목록에서 몸무게가 75보다 큰 사람은 2명입니다.
# 학생 체중(kg)
# 65
# 70
# 75
# 80
# 84
# 학생들의 몸무게가 들어있는 리스트 weight, 그리고 k 값이 매개변수로 주어졌을 때, 
# k보다 몸무게가 큰 학생의 수를 세서 return 하도록 solution 함수를 작성했습니다. 
# 그러나, 코드 일부분이 잘못되어있기 때문에, 올바르게 동작하지 않습니다. 
# 주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.


# 코드
def solution(weight, k):
    answer = 0
    for w in weight:
        if w < k: 
            answer += 1
    return answer

# 실행
weights = [65,70,75,80,84]
ret = solution(weights, 70)
print( ret )