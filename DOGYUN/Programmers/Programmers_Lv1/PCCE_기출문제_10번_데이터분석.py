# data 중 조건을 만족하는 데이터만 뽑아서 정렬
# ext : 어떤 정보를 기준으로 데이터 추출할지 결정
# val_ext : 뽑아낼 정보의 기준값
# sort_by : 정보 정렬의 기준 / code(코드번호), date(제조일), maximum(최대 수량), remain(현재 수량)

def solution(data, ext, val_ext, sort_by):
    answer = []
    condition_dict = {"code": 0, "date": 1, "maximum": 2, "remain" : 3}
    for i in data:
      value = i[condition_dict[ext]]
      if value <= val_ext:
        answer.append(i)
  
    answer.sort(key = lambda x: x[condition_dict[sort_by]])
    return answer
  
print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))