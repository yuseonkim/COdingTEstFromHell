# 이분 탐색
def binary_search(arr, target):
  left, right = 0, len(arr) - 1
    
  while left <= right:
    mid = (left + right) // 2
        
    if arr[mid] == target:
      return mid  # 찾는 값이 중간 값과 일치하면 인덱스를 반환
    elif arr[mid] < target:
      left = mid + 1  # 중간 값보다 크면 오른쪽 부분 리스트에서 찾기
    else:
      right = mid - 1  # 중간 값보다 작으면 왼쪽 부분 리스트에서 찾기
    
  return -1  # 리스트에 찾는 값이 없는 경우