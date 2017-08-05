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