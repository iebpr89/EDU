# 문제 7. 파일 업로드를 위한 파일 정보를 확인하는 함수의 빈 칸 채우기
# 사용자가 파일을 업로드할 수 있는 서비스를 만드려고 합니다.
# 다만, 서비스의 보안 및 안정성을 위해 일부 파일만을 업로드 할 수 있습니다.
# 파일의 정보는 문자열로 읽을 수 있으며 다음과 같이 표준화되어 있습니다.
# "파일형식,파일명,파일크기"
# 업로드 할 수 있는 파일은 파일형식이 "jpeg" 이고, 파일크기가 1000 보다 작은 파일입니다.
# 사용자가 업로드하려는 파일들의 정보를 담은 리스트 file_info 가 매개변수로 전달될 때
# 업로드된 개수와 업로드하지 못한 개수의 순서로 return 하도록 solution 함수를 작성하려고 합니다.
# 빈 칸을 채워 전체 코드를 완성해 주세요

# 답안
def solution(file_info):
    sucess = 0
    fail = 0
    for f in file_info:
        splited = f.split(",")
        print(splited)
        if splited[0] == 'jpeg' and int(splited[2]) < 1000:
            sucess += 1
        else:
            fail += 1
    return sucess, fail

files_info = ["jpeg,all.jpg,1500","mpeg,all.mp3,500"]
sucess, fail = solution(files_info)
print( sucess, fail , sep=",")

string = "this is string constant"
splited = string.split(" ") # 공백 문자로 나눈다.
print(type(splited), splited)
