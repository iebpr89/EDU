# 문제 1. 카드 숫자 조합하여 홀수의 개수를 구하는 함수 빈 칸 채우기
# 1부터 9사이의 숫자가 적혀진 다섯 장의 카드를 하나의 세트로 하며 중복되는 숫자는 없습니다. 
# 그 중 3장의 카드를 골라 적힌 숫자의 합이 홀수인 경우가 몇 번인지를 알아내려고 합니다. 
# 예를 들어 다섯 장의 카드가 (7, 5, 6, 4, 9)인 경우 순서에 관계없이 조합할 수 있는 경우는 아래와 같습니다.
# [7 5 6], [7 5 4], [7 5 9]. [7 6 4], [7 6 9], [7 4 9]
# [5 6 4], [5 6 9], [5 4 9]
# [6 4 9]
# [7, 4, 9] 의 경우 합은 20 이 되고, [7, 6, 4] 의 경우 합은 17이 됩니다. 
# 다섯 장의 카드를 저장한 리스트 cards 가 매개변수로 전달될 때 
# 3장씩 조합하여 카드에 적힌 숫자의 합이 홀수인 경우가 몇 번인지를 
# return 하도록 solution 함수를 작성하려 합니다. 빈 칸을 채워 전체 코드를 완성해 주세요

## 답안
def solution(cards):
    answer = 0
    for i in range(3): 
        for k in range(i+1,5): 
            for m in range(k+1,5): 
                print(cards[i],cards[k],cards[m],cards[i] + cards[k] + cards[m]) 
                if (cards[i] + cards[k] + cards[m]) % 2 == 1: 
                    answer += 1
    return answer

# 실행
cards = [3,5,2,7,6]
ret = solution(cards)
print(ret)

