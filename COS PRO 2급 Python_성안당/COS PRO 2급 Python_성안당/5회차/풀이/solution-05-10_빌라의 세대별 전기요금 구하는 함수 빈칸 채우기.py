# 문제 10. 빌라의 세대별 전기요금 구하는 함수 빈 칸 채우기
# 구마동의 S 빌라에는 8 세대가 살고 있다. 매달 사용하는 전기요금은 하나로 합산하여 청구되고 
# 청구서에는 빌라 전체 총 사용량과 각 세대별 사용량이 표시되어 있습니다. 
# 청구서에 적힌 사용량은 아래의 순서로 작성되어 있습니다.
# 총사용량   1호 2호 3호 4호 5호 6호 7호 8호
# 1124      224 213 104 124 221 79 94  65
# 각 세대별로 전기요금을 걷기 위해 합산 요금을 총 사용량으로 나눈 단위 요금을 구한 후 
# 세대별 사용량에 따른 전기요금을 구하려고 합니다. 
# 이 때 단위 요금의 소수점 이하는 무조건 올림하여 1로 더해서 계산하고 
# 남는 금액은 공용 회비로 사용하기로 하였습니다. 
# 예를 들어 단위 요금이 209.866 인 경우 210 으로 계산합니다. 
# S 빌라의 전기 사용량을 위의 순서대로 담은 리스트 wats, 합산 전기 요금 bill 이 매개변수로 전달될 때 
# 각 세대별 전기요금을 담은 리스트를 return 하도록 solutioin 함수를 작성했습니다. 
# 빈 칸을 채워 올바르게 동작하도록 완성해주세요

## 답안
def solution(wats, bill):
    result = [0 for _ in range(8)]
    unit_price = int(bill / wats[0]) + 1    # 소수점 이하를 버리는 대신 1을 더한다.
    for i in range(len(wats)-1):            # range(8), range(len(result)) 도 가능.
        result[i] = wats[i+1] * unit_price  # result 와 wats 의 길이가 다르다.
    return result


## 실행
bill = 1275
wat = [10,20,60,30,10,20,60,30]
t = 0
for i in wat:
    t += i
wats = [t]+wat    # wats.extends(wat)
print(wats)

ret = solution(wats,bill)
print( ret )

t = 0
for i in ret:
    t += i
print(t)

