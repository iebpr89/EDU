# 문제 7. 판매 이익금을 구하는 함수 수정하기
# 어느 무역상사에서는 여러 나라의 아이디어 상품을 들여와 판매하고 있습니다. 
# 상품을 들여오는 원가에 각각 다른 비율로 이익률을 더하여 판매가로 산정하고 있습니다. 
# 원가                          이익률
# 5000원 미만                   25%
# 5000원 이상 15,000원 미만     20%
# 15,000원 이상 100,000원 미만  15%
# 100,000원 이상                10%
# 몇 종류의 상품을 모두 동일한 수량을 들여와서 최소 이익금를 알아보려고 합니다. 
# 예시) 전달되는 리스트는 아래 표와 같이 각 상품별 원가와 수량을 행 단위로 저장합니다.
#       원가    수량
# 상품1 6000    20
# 상품2 80000   100
# 상품3 4000    90
# 상품의 원가와 구매 수량을 담은 리스트 price 가 매개변수로 전달될 때 
# 가장 작은 이익금이 얼마인지를 return 하도록 solution 함수를 작성했습니다. 
# 그러나 코드 일부분이 잘못되어 있어서 올바르게 동작하지 않습니다. 
# 주어진 코드를 한 줄만 변경하여 올바르게 동작하도록 수정해주세요 

# 답안
def func_a(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min

def solution(price):
    sales = [0 for _ in range(len(price))]
    for i in price:
        if i[0] < 5000:
            percent = 0.25
        elif i[0] < 15000:
            percent = 0.20
        elif i[0] < 100000:
            percent = 0.15
        else:
            percent = 0.1
        sales[i] = i[0] * percent * i[1]    # 계산방법 틀림
    return func_a(sales)


# 실행
price = [
    [50000,10],
    [15000,20],
    [5000,40],
    [150000,100],
]
ret = solution(price)
print( ret )
