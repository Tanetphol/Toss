street = 'HH...'
c=0
ls=list(street)
for i in range(len(ls)):
    if ls[i]=="H":
        if i > 0 and ls[i-1]== "B":
            continue
        if i+1<len(ls) and ls[i+1]==".":
            ls[i+1]="B"
            c+=1
        elif i>0 and ls[i-1] == ".":
            ls[i-1] = "B"
        else:
            print('end')
print(ls)