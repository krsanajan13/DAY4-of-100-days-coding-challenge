s1="Sanjana"
d1={}
for i in s1:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
for j in d1:
    if d1[j]!=1:
        print(j)