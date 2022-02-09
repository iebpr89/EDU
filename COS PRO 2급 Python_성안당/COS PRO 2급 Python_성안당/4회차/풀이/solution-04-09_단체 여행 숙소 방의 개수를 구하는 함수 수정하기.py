# 문제 9. 단체 여행 숙소 방의 개수를 구하는 함수 수정하기
# A 초등학교에서는 단체로 2박 3일 여행을 가기로 했습니다. 
# 1학년부터 6학년까지 학생들이 묵을 방을 배정해야 합니다. 
# 같은 학년끼리만 방을 배정해야 하며 방 하나에 한 명만 배정하는 것도 가능합니다. 
# 방 하나에 배정할 수 있는 최대 인원 수가 k 일 때, 
# 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하려고 합니다. 
# 예를 들어, 학생 수가 다음 표와 같고 k = 4 일 때 17개의 방이 필요합니다.
# 학년  인원    방 개수
# 1     13      4
# 2     16      4
# 3     9       3
# 4     2       1
# 5     10      3
# 6     7       2
# 학년별 인원수가 1학년부터 순서대로 저장된 리스트 arr, 방 하나의 최대인원 수 k 가 
# 매개변수로 전달될 때 필요한 방의 개수를 return 하는 solution 함수를 작성했습니다. 
# 그러나 코드 일부분이 잘못되어 있어서 올바르게 동작하지 않습니다. 
# 주어진 코드에서 한 줄만 변경하여 올바르게 동작하도록 수정해주세요.

## 답안
def solution(arr, k):
    answer = 0
    for i in arr:
        answer += i//k     # answer 는 방의 개수, i 는 각 학년의 인원 수 이다.
        if i % k != 0:
            answer += 1
    return answer

# 실행
arr = [13,16,9,2,10,7]
k = 4
ret = solution(arr,k)
print(ret)

