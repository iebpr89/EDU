# 문제 3. 방문객 수의 차이를 구하는 함수의 빈 칸 채우기
# 씨에비 극장에서 n일 동안 매일 방문객 수를 조사했습니다. 
# 이때, 가장 많은 방문객 수와 두 번째로 많은 방문객 수의 차이를 구하려고 합니다. 
# 단, 방문객의 수가 같은 날은 없다고 가정합니다. 
# 이를 위해 다음과 같이 4단계로 간단히 프로그램 구조를 작성했습니다.
# 1. 입력으로 주어진 리스트에서 가장 많은 방문객 수를 찾습니다.
# 2. 1번 단계에서 찾은 값을 제외하고, 나머지 값들로 이루어진 새로운 리스트를 만듭니다.
# 3. 2번 단계에서 만든 새로운 리스트에서 가장 큰 방문객의 수를 찾습니다.
# 4. 1번 단계와 3번 단계에서 구한 값의 차이를 구합니다.
# n일 동안의 방문객 수가 들어있는 리스트 visitor 가 매개변수로 주어질 때, 
# 가장 많은 방문객 수와 두 번째로 많은 방문객 수의 차이를 return 하도록 solution 함수를 작성하려 합니다. 
# 코드가 올바르게 동작할 수 있도록 빈칸를 알맞게 채워주세요.



## 답안
def func_a(arr, num): 
    ret = []
    for i in arr:
        if i != num:    # arr 리스트에서 num 을 제외하고 복사
            ret.append(i)
    return ret

def func_b(a, b):   # 두 값의 차이(뺄셈의 결과)를 반환하는 함수
    if a >= b:
        return a - b
    else:
        return b - a

def func_c(arr):    # arr 리스트 요소 중 최대값을 반환하는 함수
    ret = -1
    for i in arr:
        if ret < i:
            ret = i
    return ret

def solution(visitor):  
    max_first = func_c( visitor )                    # 1. 가장 많은 방문객 수
    visitor_removed = func_a( visitor, max_first)   # 2. 1항이 제거된 리스트
    max_second = func_c( visitor_removed)         # 3. 가장 많은 방문객 수
    answer = func_b( max_first, max_second)            # 4. 구한 값의 차이 구하기
    return answer

visitor = [1,3,2,4,5,3,6,3,7,4,5,7]
ret = solution(visitor)
print(ret)





