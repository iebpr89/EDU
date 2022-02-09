# 문제 9. 중복되는 문자를 제거하는 함수 수정하기
# 알파벳 문자열이 주어질 때, 연속하는 중복 문자를 삭제하려고 합니다. 
# 예를 들어, "senteeeencccccceeee"라는 문자열이 주어진다면, 
# “eeee" 은 ”e" 로, “cccccceeee” 는 “ce" 로 연속하여 중복되는 문자를 제외하여 
# "sentence"라는 결과물이 나옵니다.
# 영어 소문자 알파벳으로 이루어진 임의의 문자열 characters가 매개변수로 주어질 때, 
# 연속하는 중복 문자들을 하나만 남기고 삭제한 결과를 return 하도록 solution 함수를 작성하였습니다. 
# 그러나, 코드 일부분이 잘못되어있기 때문에, 올바르게 동작하지 않습니다. 
# 주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요

# 답안
def solution(characters):
    result = [characters[0]]    # 처음 문자 1개를 대입해둔다.
    no = 0                    # result[no]에 characters[0] 문자가 있다.
    for i in range(1,len(characters)):
        if result[no] != characters[i]:
            result.append(characters[i])
            no += 1
    return ''.join(result)

# 생각해볼 풀이
# def solution(characters):
	# result = [characters[0]]
# 	for i in range(1,len(characters)):
# 		if characters[i-1] != characters[i]:
# 			result.append(characters[i])    # 현재 문자[i] 를 저장한다.
# 	return ''.join(result)

#sentence = "reeplay"
sentence = "senteeeencccccceeee"
ret = solution(sentence)
print(ret)

