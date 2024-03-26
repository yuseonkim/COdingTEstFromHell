# 화살표의 종류와 길이 알아내기
# [[type, length]] return
# 왼쪽, 오른쪽, 양쪽이 각각 -1, 1, 0

def solution(image):
    arrows = []
    current_arrow = []

    for char in image:
        if char == '-':
            current_arrow.append(char)
        elif char == '<':
            if current_arrow:
                arrows.append([-1, len(current_arrow)])
                current_arrow = []
        elif char == '>':
            if current_arrow:
                arrows.append([1, len(current_arrow)])
                current_arrow = []

    # 마지막으로 남아 있는 화살표 처리
    if current_arrow:
        if image[0] == '-':
            arrows.append([1, len(current_arrow)])
        else:
            arrows.append([-1, len(current_arrow)])

    return arrows

  
print(solution('---><-----><-'))