# 문제 6. 문자열 내 정수들의 총합 구하는 함수 빈 칸 채우기
# 문자열에서 정수를 추출하여 총합을 출력하는 프로그램을 만들려고 합니다. 
# 예를 들어 “korean world cup 2018. olympic stadium 10, 11 pm 1." 인 문자열에서 
# 정수는 2018, 10, 11, 1 이며 이들의 총합은 2040 입니다. 
# 임의의 문자열 string 이 매개변수로 전달할 때 그 문자열 내의 정수들을 추출하여 총합을 return 하도록 
# solution 함수 작성하려 합니다. 빈 칸을 알맞게 채워 올바르게 작성하도록 완성해주세요.

## 답안
def solution(string):
    answer = 0
    number = 0
    s = string+' '
    for c in s:
        if '0'<= c and c <= '9':
            print(c, int(c))
            number = number * 10 + int(c)
        else:
            answer += number
            number = 0
    return answer

string = "12 korean34 usa"
ret = solution(string)
print(ret)
