# 문제 3. 학습 대상자 수를 구하는 함수 수정하기
# A 고등학교에서는 수준별 수능 대비반을 운영하려고 합니다. 
# 용기반은 최근 수능 모의고사에서 200점 이하의 성적을 취득한 학생만을 대상으로 합니다. 
# 학생들의 모의고사 성적이 들어있는 리스트 scores가 매개변수로 주어질 때, 
# 용기반 대상자들의 인원수를 return 하도록 solution 함수를 작성했습니다. 
# 그러나, 코드 일부분이 잘못되어있기 때문에 오류가 발생합니다. 
# 주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.
# scores 에 저장되는 값은 0 이상 400 이하의 정수입니다.

# 코드
def solution(scores):
	count = 0
	for s in range(scores): 
		if scores[s] <= 200:
			count += 1
	return count

# 실행
scores = [100,200,300,400]
ret = solution(scores)
print( ret )

