# i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때 k번째에 있는 수 구하기
# array : 숫자가 담긴 배열
# commands : 구하기 위한 규칙 / 각 원소의 길이는 3

def solution(array, commands):
    answer = []
    for command in commands:
      i, j, k = command
      sliced_list = array[i-1:j]
      sliced_list.sort()
      answer.append(sliced_list[k-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])