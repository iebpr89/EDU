# 문제 8. 이름에 특정 문자가 포함된 개수를 구하는 함수 수정하기
# 건물의 1층 출입문 옆에는 입주한 회사들의 이름이 적혀 있는 안내판이 있습니다. 
# 회사들의 명단에서 이름에 'A' 또는 'K'가 들어가는 회사의 수를 구하려고 합니다. 
# 예를 들어 'Adios'에는 'A'가 들어가 있으며, "Kickboard Association" 에는 'A' 와 'K' 가 모두 들어있습니다.
# 안내판의 회사명들이 들어있는 리스트 name_list 가 매개변수로 주어졌을 때, 
# 회사명에 'A' 나 'K'가 들어가는 회사명의 수를 세서 return 하도록 solution 함수를 작성했습니다. 
# 그러나, 코드 일부분이 잘못되어있기 때문에, 올바르게 동작하지 않습니다. 
# 주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

## 답안
def solution(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            if char.find('A') > -1 or char.find('K') > -1:    # find 는 -1 을 반환, -1은 True
                answer += 1
                break
    return answer

names = ['Adios', "Kickboard Association", "google"]
ret = solution(names)
print(ret)


name = "james"
ret = name.find('k')
print(ret)
if ret:
    print('if 조건식이 참일 때')
