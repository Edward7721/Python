#remove dublicates from list:
#with set:
l = [1,2,3,4,4,4,5,1,2,7,8,8,10]
s = set(l)
print(s)

#with fromkeys:
dic = {}.fromkeys(l,1);
for item in dic:
    print(item)


