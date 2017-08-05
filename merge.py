'''
Merging two sorted list
We have two sorted lists, and we want to write a function to merge the two lists into one sorted list:
a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
'''
def merge(a,b):
    lena=len(a)
    lenb=len(b)
    ab=[]
    i, j =0, 0
    while (i<lena and j<lenb):
        if(a[i]<b[j]):
            ab.append(a[i])
            print(ab)
            i+=1
        else:
            ab.append(b[j])
            print(ab)
            j+=1

    if(i<lenb):
        ab.extend(b[j:lenb])
    if(j<lena):
        ab.extend(a[i:lena])

    print (ab)

merge(a,b)