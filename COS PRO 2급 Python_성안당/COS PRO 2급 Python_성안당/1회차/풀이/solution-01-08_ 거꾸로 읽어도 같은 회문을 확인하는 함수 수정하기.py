# 문제 8. 거꾸로 읽어도 같은 회문을 확인하는 함수 수정하기
# 앞에서부터 읽을 때와 뒤에서부터 읽을 때 똑같은 단어 또는 문장을 “회문“이라고 합니다. 예를 들어서 racecar, noon은 회문입니다.
# 소문자 알파벳, 공백(' '), 그리고 마침표('.')로 이루어진 문장이 회문인지 점검하려 합니다. 문장 내에서 알파벳만 추출하였을 때만을 고려하려고 합니다. 예를 들어, "Never odd or even."과 같은 문장은 회문입니다.
# 소문자 알파벳, 공백(' '), 그리고 마침표('.')로 이루어진 문장 sentence가 주어질 때 회문인지 아닌지를 return 하도록 solution 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.

# 답안
def solution(sentence):
    filtered = []
    for s in sentence:
        if s != ' ' and s != '.':
            filtered.append(s)
    before = ''.join(filtered)    # 공백과 마침표를 제외한 상태
    print(before)
    filtered.reverse()
    after = ''.join(filtered)
    print(after)
    return before == after

sentence = "r     ace c.a.ra"
ret = solution(sentence)
print( ret )
