# 지원자들의 자격증을 보고 면접 대상자 뽑기
# 자격증은 1~n번으로 분류 / 해당 자격을 증명하는 레벨이 존재 -> 레벨이 높을수록 높은 실력 / 자격증이 없으면 레벨 0
# 필수 자격증이 없으면 무조건 제외
# 회사에서 요구하는 필수 자격을 모두 가지고 있고, 보유한 자격증 레벨 합이 m이상인 지원자 뽑기
# 필수 자격증의 번호 : licenses / 지원자들이 보유한 자격증 레벨을 담은 2차원 정수 배열 : spec
# 면접 대상자인 지원자 번호를 오름차순으로 1차원 정수 배열에 담아 return

def solution(n, m, licenses, spec):
  answer = []
  for i in range(len(spec)): # 0,1,2,3
    for license in licenses:
      if spec[i][license-1] == 0:
        break
      else:
        if m > sum(spec[i]):
          break
        else:
          answer.append(i+1)
          break
  
  return answer

print(solution(5, 10, [2, 3], [[2,2,1,2,2], [4,0,3,3,2], [5,1,2,4,0], [3,1,1,2,3]]))