#!/usr/bin/python
numbers = []	
a, b = 0, 1
step = 0
while step < 10:
    numbers.append(a)
    print("a", a, "b" , b)
    a, b = b, a + b
    step = step+1
print(numbers)
	
#output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
