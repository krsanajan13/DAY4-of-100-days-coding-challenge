s1="Hi good morning"
s2=s1.split()
res=""
for word in s2:
    rev=""
    for char in word:
        rev=char+rev
    res+=" "+rev
print(res)