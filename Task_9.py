print('Type an integer number:')
num = int(input())
answer = 1
for i in range(num):
    answer = answer * (i+1)
answer = str(answer)
print('Your answer:' + answer)