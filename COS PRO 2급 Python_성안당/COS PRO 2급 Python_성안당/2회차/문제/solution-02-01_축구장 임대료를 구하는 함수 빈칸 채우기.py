# 문제 1. 축구장 임대료 구하는 함수 빈 칸 채우기
# 우리 지역에서 개최하는 사회인 축구대회에 총 8팀이 참가 신청을 하였습니다. 
# 각 팀이 다른 모든 팀과 한 번씩 경기를 진행하려고 합니다. 
# 각 팀은 하루에 한 경기만 참여할 수 있으며 쉬는 날도 있습니다. 
# 대회에 사용할 축구장을 임대해야 하기 때문에 임대료를 계산하여 예산 신청을 해야 합니다.
# 대회에 참가하는 팀 수 n 과 축구장의 하루 임대료 price 가 매개변수로 주어질 때 
# 전체 대회 기간에 대한 임대료를 계산하여 return 하도록 solution 함수를 작성했습니다.   
# 코드가 올바르게 동작할 수 있도록 빈 칸을 알맞게 채워주세요.

# 코드
def solution(n, price):
    games = ______ // 2
    per_day = ______ // 2
    answer = (games // per_day) * price
    return answer

# 실행
teams = 7
price = 100000
ret1 = solution(teams, price)
print(ret1)
