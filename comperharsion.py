#reverse string by slicing:
word = '123456'
print(word, 'reverse word:', word[::-1])

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
print([x for x in nums])

# I want 'n*n' for each 'n' in nums
print([n*n for n in nums])

# I want 'n*n' for each 'n' in nums Using a map + lambda
# lambda is function:
f = lambda n: n*n
print (f(4))
# lambda used with map. Map accepted two arguments function and sequence.
num1 = map(lambda n: n*n, nums)
print([n for n in num1])

# I want 'n' for each 'n' in nums if 'n' is even
print([x for x in nums if x%2==0])

# I want 'n*n' for each 'n' in nums if 'n' is even Using a filter + lambda
list2= filter(lambda y: y%2==0, nums)
print([n for n in  list2])
