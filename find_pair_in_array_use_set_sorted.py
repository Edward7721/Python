'''Write a function / method that takes two input parameters: an integer array and an integer sum and print
all pairs of integers in the array that add up to the target sum.
'''

arr =  [8, 2, -5, 0, -1, 6, 12, 8, -2, 10, 9, 15, -6]
sum: 10.
#Pairs: (8, 2), (-5, 15), (12, -2), (0, 10)

def pair(arr, sum):
    res = []
    s = set(sorted(arr))
    a = list(s)
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
           if a[i] + a[j] == sum:
                print("found:", a[i], a[j])



def isExist(res,pair):
   reverse =[]
   if res.count(pair)==1:
      return True
   reverse.append(pair[1])
   reverse.append(pair[0])
   if res.count(reverse)==1:
       return True
   return False

pair(arr, 10)