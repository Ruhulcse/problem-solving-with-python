n=int(input())
while n!=0:
    word=str(input())
    n-=1
    if len(word)>10:
        first=word[0]
        last=word[-1]
        lenght=str(len(word)-2)
        print(first+lenght+last)
    else:
        print(word)

