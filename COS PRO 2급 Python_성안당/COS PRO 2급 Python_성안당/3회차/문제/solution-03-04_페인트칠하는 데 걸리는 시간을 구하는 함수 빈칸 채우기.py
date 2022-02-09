# 문제 4. 페인트 칠하는데 걸리는 시간을 구하는 함수 빈 칸 채우기
# 새로 이사 갈 집을 예쁜 색으로 페인트칠을 하려고 합니다. 
# 세 명 친구 A, B, C 가 일을 돕겠다고 합니다. 
# 각 친구들이 칠을 하는 속도가 달라서 같은 크기의 벽을 A는 1시간, B는 2시간, C는 4시간이 걸립니다. 
# A, B, C 세 사람이 함께 이 집을 칠하는 몇 시간이 걸리는지 알기 위해 
# 이 집의 벽의 개수 walls 가 매개변수로 전달될 때 모든 벽을 칠하는데 걸리는 시간을 
# return 하도록 solution 함수를 작성하려 합니다. 
# 빈 칸을 채워 전체 코드가 올바르게 실행되도록 완성해주세요. 

# 제한조건
# 전달되는 벽의 개수는 3 이상 자연수이며 모든 벽의 크기는 동일합니다.
# 하나의 벽을 같이 칠하는 경우는 없습니다.

# 코드
def solution(walls):
    answer = 0
    painted_walls = 0
    hour = 1
    while painted_walls < walls:
        painted_walls = ( hour ) + ( ______ ) + ( ______ )
        hour += 1
    answer = ______
    return answer

# 실행
walls = 5
ret = solution(walls)
print(ret)

