num = int(input())

if (1<=num and num<=1000):
    i = 1
    while(i<=num):
        if(i%2==1):
            print(i)
        i +=1
    

# outra forma
# i=1   while (1<=num): print(i)   i+=2