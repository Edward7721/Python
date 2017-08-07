#Using map, filter, reduce, write a code that create a list of (n)**2 for range(10) for even integers:

#using list comreherising:
l = [x**2 for x in range(10) if x%2==0]
for n in l:
    print (n)

#using filter and map
l1 = filter(lambda x:x % 2 == 0, [x for x in range(10)] )

l11 = map(lambda x: x**2, l1)
for n11 in l11:
    print (n11)
