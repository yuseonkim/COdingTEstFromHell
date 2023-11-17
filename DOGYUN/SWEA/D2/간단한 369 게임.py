# 3, 6, 9 있으면 - / 2개 있으면 --

text_array = ['3', '6', '9']
N = int(input())

a = ''
for i in range(1, N+1):
    i = str(i) # 13
    count = 0
    for j in i: # 1 / 3
        if j in text_array:
            count += 1

    if count != 0:
        i = '-' * count

    a += i
    a += ' '
print(a)