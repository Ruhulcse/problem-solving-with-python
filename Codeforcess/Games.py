a=[]
b=[]
c=0
for i in range(int(input())):
    x,y=map(int,input().split(" "))
    a.append(x)
    b.append(y)
for i in a:
    for j in b:
        if i==j:
            c+=1
print(c)
