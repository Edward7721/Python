'''
find frequency of word in text:
'''
str = "aaa bbb ccc aaa bbb kkk aaa"

def count_words(str):
    list = str.split(" ");
    dic = {}.fromkeys(list,0)
    for word in list:
        dic[word]+=1
    print(dic)

count_words(str)

"""
Find sum of all numbers in the string 'sdf2tg dff234hh d999njk1hj'
sum = 1236 (2 + 234 + 999 + 1)
"""

def sum1(str):
    n=0;
    num =[]
    all=[]
    sum = 0
    while(n<len(str)):
        if(str[n].isdigit()):
            num.append(str[n])
            n=n +1
        else:
            if(len(num) >0):
                all.append(num)
                num = []
            n=n+1
    for num in all:
        sum  = sum + eval("".join(num))
    return sum

print(sum1("111 666"))
# output 2+234+999+1=1236
