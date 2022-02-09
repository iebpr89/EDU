# 문제 2. 무게를 재기 위해 필요한 추의 개수 구하는 함수 빈 칸 채우기
# 실험실에서 양팔저울을 이용하여 무게를 측정하려고 합니다. 
# 무게 측정 시 사용할 수 있는 추는 g 단위로 [ 1, 2, 3, 5, 7, 11, 13, 17, 19, 23 ] 
# 열 가지로 모두 1개씩 구비되어 있습니다. 
# 실험실에서 다루는 대상물은 100g 을 넘는 경우는 없으며 
# 여러 명의 연구원이 실험을 위해 추를 사용하기 때문에 남아 있는 추는 매번 다릅니다. 
# 남아있는 추로 어떤 구슬의 무게를 잴 때 양팔 저울이 균형을 이루는 추의 개수가 가장 적은 것을 구하려고 합니다. 
# 가장 작은 단위부터 순서대로 추를 저장한 리스트 arr, 구슬의 무게 payload 가 매개변수로 전달될 때 
# 균형을 이루었을 때 가장 적은 추의 개수를 return 하도록 solution 함수를 작성하려고 합니다. 
# 빈 칸을 채워 올바르게 동작하도록 완성해주세요.

# 제한조건
# 남아있는 추로 무게를 젤 수 없는 경우 0 을 반환합니다.
# 모든 단위의 추는 1개씩만 존재합니다.
# 구슬의 무게는 1 이상 100 이하의 정수입니다.

# 코드
def func_a(arr):
    total = 0
    for i in arr:
        total += i
    return total

def solution(arr, payload):
    answer = 0
    sum = func_a(arr)
    if sum >= payload:
        arr.______
        arr.reverse()
        weight = 0
        for i in range(len(arr)):
            diff = ______
            if arr[i] <= diff:
                weight += arr[i]
                answer += 1
        if weight != payload:
            answer = 0
    return answer

# 실행
arr = [ 2, 3, 5, 7, 13, 17, 19, 23 ]
payload = 25
ret = solution(arr,payload)
print(ret)
