l1=[10,20,40,5,90,100,0]
f_max=s_max=float('-inf')
for i in l1:
    if i>f_max:
        s_max=f_max
        f_max=i
    # elif i>s_max and i!=f_max:
    #     s_max=i
print(s_max)