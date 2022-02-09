# 문제 2. 3개 사면 추가 하나는 50% 할인 행사의 금액을 계산하는 함수 빈 칸 채우기
# 새로 개업한 편의점에서 홍보를 위한 행사를 진행하고 있습니다. 
# 편의점 내 어떤 상품이든 3 개를 사면 추가로 하나의 상품을 50% 할인된 가격으로 살 수 있습니다. 
# 3개 미만인 경우에는 적용되지 않습니다. 계산은 물건이 나열된 순서대로 하며 도중에 바꿀 수는 없습니다. 
# 예를 들어 가격이 [ 100 500 200 400 300 ] 인 상품들을 가져온 경우, 
# 지불할 금액은 100 + 500 + 200 + (400 x 50%) + 300 과 같이 계산됩니다.  
# 구매할 상품의 가격을 순서대로 저장한 리스트 arr 가 매개변수로 전달될 때 
# 지불할 금액을 return 하도록 solution 함수를 작성하려 합니다. 빈 칸을 채워 전체 코드를 완성해주세요.

# 답안
def solution(arr):
    answer = 0
    for i in range(len(arr)):
        price = arr[i]
        if (i+1) % 4 == 0:
            price //= 2
        answer += price
    return answer

# 실행
arr = [ 100, 500, 200, 400, 300 ]
ret = solution(arr)
print( ret )

