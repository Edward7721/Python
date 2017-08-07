
def reverse(str):
   l = str.split()
   res = []
   for char in l:
        print(char)
        res.insert(0,char)
   return ' '.join(res)

print( reverse("1 2 3 4 5"))
# result will be:
# 54321
