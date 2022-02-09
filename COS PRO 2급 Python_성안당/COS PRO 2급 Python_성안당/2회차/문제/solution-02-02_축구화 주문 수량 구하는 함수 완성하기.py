# 문제 2. 축구화 주문 수량 구하는 함수 완성하기
# 알랑 중학교의 축구팀에서는 단체로 축구화를 주문하기 위해 학생별로 신발 사이즈를 조사했습니다. 
# 선택할 수 있는 축구화 사이즈는 작은 순서대로 "7", "7.5", "8", "8.5", "9", "9.5" 총 6종류가 있습니다. 
# 학생별로 원하는 사이즈를 조사한 결과가 들어있는 리스트 shoes_size가 매개변수로 주어질 때, 
# 사이즈별로 축구화가 몇 개씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return 하도록 
# solution 함수를 완성해주세요.

# 코드
def solution(shoes_size):
   answer = []
   return answer


# 실행
shoes_size = ["7", "7.5", "8", "8.5", "9", "9.5"]
ret = solution(shoes_size)
print(ret)

#answer = [0 for _ in range(6)]
answer = []
for _ in range(6):
    answer.append(0)
print(answer)
