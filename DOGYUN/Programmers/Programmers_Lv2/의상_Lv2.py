# 의상 고르기
# 같은 종류의 의상을 고를 수는 없음
# 하루에 최소 한 개의 의상을 입음
# 각 행은 [의상의 이름, 의상의 종류]로 이루어짐

def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    # default Value를 넣어줄 수 있어서 key 값 없어도 사용 가능
    for cloth, type in clothes:
      clothes_dict[type] = clothes_dict.get(type, 0) + 1
    
    for type in clothes_dict:
      answer *= (clothes_dict[type]+1)
      
    return answer-1
  
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))