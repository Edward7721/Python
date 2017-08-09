"""
Print triangle, below example for n = 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""

def tringle(num):
    print (1)
    p= [1,1]
    print([i for i in p])
    c=[]
    row=2
    while(row <= num):
        c.append(1)
        n=0
        while(n<len(p)-1):
            c.append(p[n+1]+p[n])
            n +=1
        c.append(1)
        print([i for i in c])
        p = c
        c=[]
        row +=1

tringle(5)