# 문제 5. 카드 게임 승자 알아내는 함수 작성하기
# 숫자가 표시된 카드로 민희와 민호가 게임을 하려고 합니다. 
# 각각 1 에서 13 까지 수가 하나씩 표시된 13장의 카드뭉치가 주어지며 
# 두 사람은 카드를 임의의 순서로 섞은 후 숫자가 보이지 않게 한 줄로 늘어놓고 게임을 시작합니다. 
# 게임의 규칙은 아래와 같습니다.
# 1) 게임 도중 카드의 순서를 바꿀 수는 없다. 
# 2) 첫 번째 놓인 카드부터 시작하여 순서대로 뒤집는다. 
# 3) 카드를 뒤집어서 표시된 수가 높은 쪽이 승리하며 같은 경우에는 무승부로 한다. 
# 4) 모든 카드를 뒤집은 후 이긴 횟수가 많은 쪽이 최종 승자가 된다. 
# 카드뭉치를 각각 민호는 mho_cards, 민희는 mhe_cards 리스트 담아 매개변수로 전달될 때
# 민호가 이긴 경우 1, 민희가 이긴 경우 0, 무승부인 경우 -1 을 return 하도록 solution 함수를 완성해주세요.

## 답안
def solution(mho_cards, mhe_cards):
    result = -1
    minho = 0
    minhee = 0
    for i in range(len(mho_cards)):
        if mho_cards[i] > mhe_cards[i]:
            minho += 1
        elif mho_cards[i] < mhe_cards[i]:
            minhee += 1
    if minho > minhee:
        result = 1
    elif minho < minhee:
        result = 0
    return result

mho_cards = [1,2,3,4,5,7,6,8,9,10,11,12,13]
mhe_cards = [2,1,3,4,5,9,6,7,8,10,11,12,13]
ret = solution(mho_cards,mhe_cards)
print(ret)
