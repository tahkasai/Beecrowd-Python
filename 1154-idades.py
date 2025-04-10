media = 0
i = 0

while True:
    num = int(input())
    if (num<0):
        break
    media += num
    i+=1
print(f'{(media/i):.2f}')