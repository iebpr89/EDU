# 문제 10. 문자열들을 처리하는 시간 구하는 함수 수정하기
# 1대의 컴퓨터가 길이 4인 문자열을 처리하는데 1분이 걸린다고 합니다. 
# 문자열의 길이가 13인 경우 4 단위로 나누어서 4번 처리하게 되어 4분이 걸리게 됩니다. 
# 여러 개의 문자열을 저장한 리스트 strings 가 매개변수로 전달될 때 
# 처리에 소요되는 시간을 구하여 return 하도록 solution 함수를 작성했습니다. 
# 그러나 코드 일부분이 잘못되어 있어서 올바르게 동작하지 않습니다. 
# 주어진 코드에서 한 줄만 변경하여 모든 입력에 대해 올바르게 동작하도록 수정하세요

# 제한사항
# 컴퓨터는 1대이며 동시에 여러 개의 문자열을 처리할 수 없습니다.

## 답안
def solution(strings):
    result = 0
    for s in strings:
        length = len(s)
        result += (length // 4)
        if length % 4 != 0:    # 남는 문자가 3개 이하일 때 한 번 처리
            result += 1
    return result

strings = ["1234","1234","1234"]
ret = solution(strings)
print(ret)


