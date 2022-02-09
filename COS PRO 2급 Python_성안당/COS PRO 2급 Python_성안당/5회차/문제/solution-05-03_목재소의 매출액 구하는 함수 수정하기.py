# 문제 3. 목재소의 매출액 구하는 함수 수정하기
# 나무를 파는 가게를 운영하는 A 사장은 길이 8인 목재만을 취급하며 주문받은 길이만큼 잘라 판매합니다. 
# 예를 들어 주문에 따라 길이 2와 6으로 잘라 2개의 목재로 팔 수도 있고, 길이 2짜리 4개로 잘라 팔 수도 있습니다. 
# 목재는 길이 1당 3000원에 판매하고 있습니다. 
# A 사장이 가지고 있는 목재의 개수 N 과 주문받은 목재 길이를 저장한 리스트 orders 가 매개변수로 전달될 때 
# 매출액을 return 하도록 solution 함수를 작성했습니다. 
# 그러나 코드 일부분이 잘못되어 올바르게 동작하지 않습니다. 
# 주어진 코드에서 한 줄만 변경하여 올바르게 동작하도록 수정해주세요.

# 제한조건
# 목재를 자를때 생기는 오차는 생각하지 않는다.
# 주문 길이는 1 이상 8 이하이며 같은 길이의 주문이 존재할 수 있다.

# 코드
def func_a(a, length):
    for i in range(len(a)):
        if a[i] >= length:
            return i
    return -1

def solution(N, orders):
    material = [0 for _ in range(N)]
    k = 0
    price = 0
    for o in orders:
        k = func_a(material, o)
        if k >= 0:
            material[k] -= o
            price += 3000 * o
    return price

# 실행
orders = [1,3,5,7,8]
ret = solution(10, orders)
print(ret)




