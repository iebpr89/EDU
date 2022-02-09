# 문제 5. 대괄호 쌍의 개수 세는 함수 빈 칸 채우기
# 문자열을 검사하여 리스트가 몇 개가 있는지를 알아내려고 합니다. 
# 리스트는 ‘[’ 로 시작되어 ‘]’ 로 끝나는 구간으로 정의하였습니다. 
# 예를 들어 문자열이 “kim, [10,20,30] jung [30,20]" 인 경우 
# 리스트는 ”[10,20,30]”, ”[30,20]” 2 개입니다. 
# 리스트는 다음과 같이 중첩될 수 있으며 “[ kim [10,20,30], jung [30,20] ]" 
# 모든 괄호는 ”여는 괄호“ 와 ”닫는 괄호“ 쌍이 되어야 합니다. 
# 다음의 절차로 코드를 실행시키려고 할 때
# 1) 문자열 내 대괄호의 쌍이 맞는지 확인
# 2) 모든 대괄호가 쌍이 될 때 문자열 속 “리스트” 개수 구하기
# 임의의 문자열 string 이 매개변수로 전달될 때 문자열 속 “리스트” 의 개수를 
# return 하도록 solution 함수를 작성하려 합니다. 빈 칸을 채워 전체 코드를 완성해주세요

# 반환 설명 
# 대괄호 쌍이 완전하지 않은 경우 -1 을 반환한다.

# 코드
def func_a(s):
    answer = ______
    cnt = 0
    for i in s:
        if i == '[':
            cnt += 1
        if i == ']':
            cnt -= 1
    if cnt == 0:
        answer = ______
    return answer

def solution(string):
    answer = 0
    if not func_a(string):
        return -1
    for i in string:
        if i == ']':
            answer += 1
    return answer

# 실행
string = "[[][]]"
ret = solution(string)
print(ret)

