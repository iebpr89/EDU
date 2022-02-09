# 문제 5. 빈도(출현 횟수)를 구하는 함수의 빈 칸 채우기
# 오매불망 까페 운영자는 가입된 회원들에게 일련번호를 부여해 두었습니다. 
# 최근 하루동안 까페에 글을 작성한 회원들의 번호가 들어있는 리스트가 있습니다. 
# 이 리스트에서 가장 많은 글을 작성한 회원의 글 개수는 
# 가장 적게 작성한 회원의 글 개수의 몇 배인지 구하려 합니다. 
# 이를 위해 다음과 같이 간단히 프로그램 구조를 작성했습니다.
# 1단계. 리스트에 들어있는 각 회원별 글 개수를 셉니다.
# 2단계. 가장 많이 작성한 회원의 글 개수를 구합니다.
# 3단계. 가장 적게 작성한 회원의 글 개수를 구합니다.
# 4단계. 가장 많이 작성 개수가 가장 적게 작성한 개수보다 몇 배 더 많은지 구합니다.
# 단, 몇 배 더 많은지 구할 때는 소수 부분은 버리고 정수만 구하면 됩니다.
# 회원번호는 자연수이며 작성된 글의 회원번호가 저장된 리스트 arr가 매개변수로 주어질 때, 
# 가장 많이 작성한 회원의 글 개수가 가장 적게 작성한 회원의 글 개수보다 몇 배 더 많은지 return 하도록 
# solution 함수를 작성하려 합니다. 
# 위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈 칸을 채워 올바르게 동작하도록 완성해주세요

# 제한조건
# 회원번호는 1 이상 1000 이하의 정수입니다.

# 코드
def func_a(arr):
    counter = [0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1                 
    return counter

def func_b(arr):
    ret = 0
    for i in arr:  
        if ret < i:      
            ret = i    
    return ret

def func_c(arr):
    ret = func_b(arr)
    for i in arr:
        if ______:
            ret = i
    return ret

def solution(arr):
    counter = func_______
    max_cnt = func_______   
    min_cnt = func_c( counter )
    return max_cnt // min_cnt


# 실행
arr = [1,2,3,1,1,2,1,2,1,2,3,1,1,1,1,1]
ret = solution(arr)
print(ret)
