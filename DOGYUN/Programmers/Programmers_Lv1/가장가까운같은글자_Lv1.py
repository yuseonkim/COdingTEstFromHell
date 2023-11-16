# s : 주어진 문자열
# 문자열보다 앞 위치에서 가장 가까운 같은 글자가 어디 있는지 찾아서 배열에 저장

def solution(s):
    answer = [] # ananab
    s_list = [ch for ch in s]
    s_list.reverse()

    for i in range(len(s_list)): # a n a n a b
        current_word = s_list[i]
        value = -1
        if i == len(s_list):
            answer.append(value)
            break
        for j in range(i+1, len(s_list)):
            if s_list[j] == current_word:
                value = j-i
                break
        answer.append(value)

    answer.reverse()
    return answer

print(solution("foobar"))
