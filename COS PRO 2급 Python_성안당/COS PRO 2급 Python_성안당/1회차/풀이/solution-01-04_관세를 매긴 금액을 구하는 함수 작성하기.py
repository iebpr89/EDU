# 문제 4. 관세를 매긴 금액을 구하는 함수 작성하기
# 율무국에서는 국가 신용 등급에 따라 수입하는 물품에 관세를 부여합니다. 
# 국가 신용 등급에 따른 관세율은 다음과 같습니다. (S = 개발도상국, G = 신진부흥국, V = 부흥국)
# 등급  관세율
# "S"   5%
# "G"   10%
# "V"   15%
# 예를 들어 등급이 "S" 인 국가에서 수입하는 물품의 가격이 1000원인 경우 
# 관세율 5% 를 적용한 가격은 1050 원이 됩니다. 
# 물품의 가격 price 와 원산지 국가의 신용 등급을 나타내는 문자열 grade가 매개변수로 주어질 때, 
# 관세율을 적용한 물품 가격을 return 하도록 solution 함수를 완성해주세요


# 답안
def solution(price, grade):
    answer = 0
    if grade == "S":    
        answer = price * 1.05
    if grade == "G":
        answer = price * 1.10    
    if grade == "V":
        answer = price * 1.15   
    return int(answer)

price = 1300
grade = "G"
ret = solution(price,grade)
print(ret)
