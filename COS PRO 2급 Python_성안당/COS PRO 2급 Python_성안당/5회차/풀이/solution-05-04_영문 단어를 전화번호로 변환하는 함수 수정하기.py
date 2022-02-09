# 문제 4. 영문 단어를 전화번호로 변환하는 함수 수정하기
# 오래 전 문자 입력 버튼이 있는 핸드폰이나 일반 전화기의 각 버튼에 숫자와 함께 
# 영어 알파벳이 할당되어 있는 경우가 종종 있습니다.
# 전화기의 버튼에 다음과 같이 인쇄되어 아래와 같이 각 숫자와 문자가 할당되어 있다고 합니다.
# 	1 ij	2 abc	3 def
# 	4 gh	5 kl	6 mn
# 	7 prs	8 tuv	9 wxy
# 		    0 oqz
# 숫자로 전화번호를 외우는 것 보다 알파벳 단어로 생각하면 전화번호를 쉽게 외울 수 있습니다. 
# 예를 들면, 번호가 941837296 인 친구의 번호를 WHITEPAWN 과 같이 외울 수 있고, 
# 단어 BULLDOG 은 전화번호로 2855304 임을 알 수도 있습니다.
# 진호는 임의의 영문 단어가 주어졌을 때, 그에 해당하는 전화번호를 찾는 프로그램을 만들려고 합니다. 
# 소문자로 이루어진 문자열 word 가 매개변수로 전달될 때 그에 해당하는 전화번호 문자열을 return 하도록
# solution 함수를 작성했습니다. 그러나 그러나 코드가 잘못 작성되어 원하는 결과가 나오지 않습니다. 
# 잘못된 한 줄을 수정하여 올바르게 동작하도록 수정해주세요.

# 매개변수 설명
# 전달되는 문자열은 공백 없이 영문 소문자로만 주어지며. 이 길이는 16자를 넘지 않습니다. 

## 답안
def solution(word):
    num2alpha = ["oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"]
    answer = ''
    for c in word:
        for i in range(len(num2alpha)):
            if num2alpha[i].find(c) != -1:    # for 문을 대체한다.
                answer += str(i)
                break
    return answer



# 실행
word = 'whitepawn'    #941837296
ret = solution(word)
print(ret)

word = 'bulldog'    #2855304
ret = solution(word)
print(ret)

word = 'netstudio'  #638788310
ret = solution(word)
print(ret)


## 비교해 보기
# def solution(word):
#     num2alpha = ["oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"]
#     answer = ''
#     for c in word:
#         for i in range(len(num2alpha)):
#             for a in num2alpha[i]:
#                 if a == c:      # i -> c
#                     answer += str(i)
#                     break
#     return answer

## 코드2
# def solution(word):
#     num2alpha = ["oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"]
#     answer = ''
#     for c in word:
#         for i in range(len(num2alpha)):
#             if num2alpha[i].find(c) != -1:
#                 answer += str(i)
#     return answer


## 
# def solution(word):
#     num2alpha = ["oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"]
#     answer = ''
#     for c in word:
#         for i in range(len(num2alpha)):
#             if num2alpha[i].find(c) != -1:
#                 answer += str(i)
#                 break
#     return answer

##
# def solution(phone,words):
#     num2alpha = ["oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"]
#     for c in phone:
#         i = int(c)
#         alphas = num2alpha[i]
#         for a in alphas:
#             for word in words:
#                 k = word.find(a)
#                 if  k != -1:
#                     print(word[k],end='')
#                     break
#     return ''


