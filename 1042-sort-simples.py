a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

if(a<b):
    p1 = a
    p2 = b
elif(a>b):
    p1 = b
    p2 = a

if(p2<c):
    p3 = c
elif(p2>c):
    troca = p2
    p2 = c
    p3 = troca

if(p1>p2):
    troca = p1
    p1 = p2
    p2 = troca

print(p1)
print(p2)
print(p3)
print()
print(a)
print(b)
print(c)
