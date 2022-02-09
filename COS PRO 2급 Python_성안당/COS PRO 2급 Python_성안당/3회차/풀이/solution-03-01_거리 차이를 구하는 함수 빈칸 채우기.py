# 문제 1. 거리 차이를 구하는 함수 빈칸 채우기
# 두 사람이 동시에 출발하여 일정한 속도로 걸어가려고 합니다. 
# 출발 이후 두 사람의 거리 차이가 10km 이상이 되는 시간을 분 단위로 구하기 위해 
# 두 사람의 시속을 각각 매개변수 a 와 b 로 전달할 때 
# 두 사람의 거리 차이가 10km 이상이 될 때의 경과시간을 return 하는 solution 함수를 작성하려 합니다. 
# 코드가 올바르게 동작하도록 빈칸을 알맞게 채워 완성해주세요.

# 제한조건
# 전달되는 속도는 km/hour 단위로 1 ~ 10 사이 정수이다.
# 전달되는 속도가 같은 경우는 없다.

## 답안
def solution(a, b):
    answer = 0
    diff = (b-a) if a < b else a-b
    answer = 10 / diff
    return answer*60

# 테스트
# def solution(a, b):
#     for i in range(1,10):
#         ad = a*i
#         bd = b*i
#         diff = bd-ad
#         print(i, ad, bd, diff )
#     return 0

a = 10
b = 12
ret = solution(a,b)
print(ret)

