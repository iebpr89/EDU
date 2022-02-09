# 문제 4. 열린 문의 개수를 구하는 함수 빈 칸 채우기
# A 고등학교에는 n 개의 교실이 있습니다. 각 교실에는 1부터 순차적으로 번호를 지정하였습니다.
# 매일 모든 수업이 종료되면 당직 직원은 모든 교실의 문을 잠근 후 막걸리를 한 병 마시는데 
# 한 잔씩 마실 때 마다 교실들의 문을 다음과 같이 열고 닫는 버릇이 있습니다. 
# 1잔째 마셨을 때 모든 교실의 문을 열어버립니다.
# 2잔째 마셨을 때는 2의 배수에 해당하는 교실의 문을 닫혀 있으면 열고 열려 있으면 닫습니다.
# 3잔째 마셨을 때는 3의 배수에 해당하는 교실의 문을 닫혀 있으면 열고 열려 있으면 닫습니다.
# 4잔째 마셨을 때는 4의 배수에 해당하는 교실의 문을 닫혀 있으면 열고 열려 있으면 닫습니다.
# 막걸리 한 병을 다 마시는데 필요한 잔 수 n 과 교실의 수 m 이 매개변수로 전달될 때
# 당직 직원이 막걸리를 다 마셨을 때 문이 열려있는 교실의 개수를 return 하도록 
# solution 함수를 작성하였습니다. 빈 칸을 채워 올바르게 동작하도록 완성해주세요

# 제한설명
# 문이 열린 상태를 0, 잠긴 상태를 1로 표현합니다.

# 코드
def solution(n,m):
    answer = 0
    OPEN, CLOSE = 0, 1
    room = [ CLOSE for i in range(______)]
    for i in range(1,n+1):
        for k in range(1, m+1):
            if k % i == 0:
                room[k] = ______
    answer = room.count(______)
    return answer

# 실행(테스트)
n = 10
m = 20
ret = solution(n,m)
print(ret)

room = [ 0 for i in range(m+1)]
print(len(room))
room[m] = 1
print((room))

room = [ 0 for i in range(1,m+1)]
print(len(room))
room[m] = 1
print((room))
