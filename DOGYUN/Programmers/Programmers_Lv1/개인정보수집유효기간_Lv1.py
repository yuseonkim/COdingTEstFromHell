# 1~n번의 개인정보 n개
# 유효기간이 12달 => 지금으로부터 12달을 더한 날짜가 파기할 수 있는 시작일
# 오늘 날짜 today  "YYYY.MM.DD" 형태
# 약관의 유효기간 담은 1차원 배열 terms
# 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacied
# 파기해야 할 개인정보의 번호를 return

def solution(today, terms, privacies):
    answer = []
    time_dictionary = dict()
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])
    
    for term in terms:
      case, month_time = term.split(' ')
      time_dictionary[case] = int(month_time)
      
    for i in range(len(privacies)):
      date, case = privacies[i].split(' ')
      pyear, pmonth, pday = date.split('.')
      pyear, pmonth, pday = int(pyear), int(pmonth), int(pday)
      pmonth += time_dictionary[case]
      
      while pmonth > 12:
        pmonth -= 12
        pyear += 1
        
      if pyear > year:
        continue
      elif pyear == year:
        if pmonth > month:
          continue
        elif pmonth == month:
          if pday > day:
            continue
    
      answer.append(i+1)
      
    return answer
  
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))