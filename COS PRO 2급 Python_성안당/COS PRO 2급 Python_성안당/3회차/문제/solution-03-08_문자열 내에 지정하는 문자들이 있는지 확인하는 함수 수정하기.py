# 문제 8. 문자열 내에 지정하는 문자들이 있는지 확인하는 함수 수정하기
# A 회사에서 운영 중인 사이트에서는 회원들의 비밀번호에 지정하는 문자들이 포함되도록 하고 있습니다. 
# 회원 가입 시 등록하는 비밀번호에는 지정하는 문자들이 최소한 하나 이상 포함되어야 회원 가입이 가능합니다. 
# 예를 들어 “Ga#9" 로 지정한 경우 비밀번호 문자열에는 ‘G', 'a', '#', '9' 문자가 
# 각각 최소 1개 이상 있어야 하며 이를 위해 사용자가 입력하는 문자열에 지정 문자들이 있는지를 
# 비교하는 기능을 만들려고 합니다. 임의 문자열 pass 와 지정 문자열 key 가 매개변수로 전달될 때 
# pass 문자열 내에 key 의 문자들이 포함되어 있는지를 검사하여 포함된 경우 1, 그렇지 않은 경우 0을 
# return 하도록 solution 함수를 작성했습니다. 
# 그러나 코드 일부분이 잘못되어 올바르게 동작하지 않습니다. 
# 주어진 코드에서 한 줄만 변경하여 모든 입력에 대해 올바르게 동작하도록 수정하세요

# 코드
def solution(password, key):
    answer = 0
    match_cnt = 0
    for k in key:
        for p in password:
            if k == p:
                match_cnt += 1
                break
    if match_cnt >= len(password):
        answer = 1
    return answer


# 실행
password = "12341sa korean uk "
key = "k1u"
ret = solution(password, key)
print(ret)

