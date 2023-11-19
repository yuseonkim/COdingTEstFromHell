# 패턴에서 반복되는 부분의 길이
# 문자열의 최대 길이는 30 / 마디의 최대 길이는 10
T = int(input())

for t in range(1, T+1):
    words = input()
    word_length = 0
    pattern = []
    next_pattern = []
    for i in range(11):
        pattern = words[:i]
        next_pattern = words[i:i*2]
        if i != 0 and pattern == next_pattern:
            word_length = len(pattern)
            break
    print('#{} {}'.format(t, word_length))