# 문제 9. 업다운 숫자게임 정답 찾는 함수 빈 칸 채우기
# 철수는 컴퓨터와 UpDown 숫자 맞추기 게임을 하려고 합니다. 
# 철수가 대답을 하고 컴퓨터가 철수가 생각한 수를 맞출 수 있도록 코드를 작성하려고 합니다. 
# 게임의 규칙은 다음과 같습니다.
# 1) 1 부터 100 사이의 정수 중에서 하나를 답으로 선택하고 진행 중 변경될 수 없다.
# 2) 컴퓨터가 부른 값이 답보다 작으면 'd' 를 입력한다.
# 3) 컴퓨터가 부른 값이 답보다 크면 ‘u' 를 입력한다.
# 4) 컴퓨터가 부른 값과 답이 같으면 'c' 를 입력한다.
# 예를 들어 철수가 정한 답이 17 일 때 컴퓨터가 부른 수가 
# 25 이면 17 < 25 로 답보다 큰 수이므로 ‘u' 를 입력합니다. 
# 컴퓨터가 부른 수가 17 이면 17 == 17 로 답과 같으므로 ’c' 를 입력하고 종료합니다. 
# 만약 1 ~ 100 사이의 모든 정수를 부른 상태이면 더 이상 부를 수가 없으므로 
# 입력한 문자에 관계없이 마지막 남은 수를 정답으로 하여 종료합니다. 
# 철수가 키보드로 입력한 문자들을 저장한 리스트 answer 가 매개변수로 전달될 때 
# 위 규칙에 맞는 답을 return 하도록 soltion 함수를 작성하려 합니다. 
# 빈 칸을 채워 전체 코드를 완성해주세요.
   

# 코드
def solution(answer):
    min = 1
    max = 100
    result = 0
    for i in answer:
        result = (max + min) / 2
        if min == max or i == 'c':
            break
        if i == 'u':
            ______
        if i == 'd':
            ______
    return result

# 실행
answer = 'udduduudc'    # 테스트 값
ret = solution(answer)
print( ret )
