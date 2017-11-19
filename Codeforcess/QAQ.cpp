string=str(input())
size=len(string)
cnt=0
for x in range(size):
    for y in range(x):
        for z in range(y):
            if string[x]+string[y]+string[z]=="QAQ":
                cnt+=1
print(cnt)
