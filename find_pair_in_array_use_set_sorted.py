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

pair(arr, 10)

# found: 0 10
# found: 2 8
# found: 12 -2
# found: 15 -5