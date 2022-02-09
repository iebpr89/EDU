# 문제 5. 정수에 3,6,9 가 포함되어 있는지 확인하는 함수의 빈 칸 채우기
# 369 게임은 순차적으로 숫자를 부르면 일정 규칙에 따라 숫자 대신 박수를 치는 게임입니다. 
# 게임의 규칙은 다음과 같습니다. 1부터 시작하고 한 사람씩 차례대로 1씩 더해가며 말합니다. 
# 말해야 하는 숫자에 3, 6, 9 가 포함되어 있는 개수만큼 손뼉을 칩니다. 
# 어떤 수 number가 매개변수로 전달될 때, 
# 1부터 number까지 순차적인 숫자들에 대해 369게임을 올바르게 진행했을 경우 박수를 총 몇 번 쳤는지를 
# return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

# 답안
def solution(number):
    count = 0
    for i in range(1, number+1):    # 1부터 number 까지 범위
        current = i
        print(current, end=':')
        while current != 0:
            unit = current % 10    # 일의 자리 떼기
            if unit == 3 or unit == 6 or unit == 9:
                count += 1
                print("짝", end='')
            current //= 10         # 일의 자리 버리기(자릿수 내림)
        print('')
    return count

number = 36
ret = solution(number)
print( ret)

for i in range(1, 10):
    print(i, end=' ')
