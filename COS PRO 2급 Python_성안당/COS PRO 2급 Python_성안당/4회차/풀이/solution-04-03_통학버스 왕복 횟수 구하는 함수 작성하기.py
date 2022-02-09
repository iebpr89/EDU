# 문제 3. 통학버스 왕복 횟수 구하는 함수 작성하기
# 새로 조성된 신도시는 큰 도로 하나를 따라 여러 아파트 단지들을 지었습니다. 
# 한 지점에 학교 하나를 신설하였습니다. 학교는 통학버스로 이 도로를 따라 왕복하여 
# 학생들을 학교로 태워 데리고 오며 통학버스는 한 대이며 정원은 12명입니다. 
# 이 통학버스는 정원을 초과하여 학생을 태울 수 없고, 모든 학생을 등교시킬 때까지 운행합니다. 
# 모든 학생을 등교시키기 위해 통학버스는 몇 번을 왕복해야하는지를 확인하려고 합니다. 
# 각 아파트 단지에 이 학교 학생들의 수를 리스트 student 담아 아파트 단지 수 apts 와 함께 
# 매개변수로 전달될 때 통학버스의 왕복 횟수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 통학버스를 타지 않는 학생은 없다.
# 학생 수는 0 이상의 정수이다.

## 답안
def solution(student, apts):
    result = 0
    total = 0
    for i in student:
        total += i
    result = total // 12
    if total % 12 != 0:
        result += 1
    return result

# 실행
student = [2,5,4,7,8,2]
ret = solution( student, len(student))
print( ret )

