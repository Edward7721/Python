'''
Objective:
==========
The objective of this assignment is to build a console line application with the data that you get from the google books api.
We will be using a simple unauthenticated google books api to get a list of books. And build a library with these books.
Please adhere to good coding practices and code quality.

API:
===
Go ahead and copy paste this link https://www.googleapis.com/books/v1/volumes?q=python on any web browser and see what it returns.
This API can also take additional parameter like https://www.googleapis.com/books/v1/volumes?q=python&maxResults=40
More information about the API can be found here https://developers.google.com/books/docs/v1/reference/volumes/list or by just googling in general.

Requirements:
============
1. The console line app should prompt the user for a search string and based on the input string the app must build the library. Please stick to popular search strings like 'dogs','cats','New York'... etc.
2. The app user must be able to save and persist the book/library data in csv file format.
3. Ability to at least sort the books by price, avg rating, rating count, published date, page count
4. The app should be able to save to and load from a csv file.
5. Bonus points for additional interesting and creative features not listed here. (Nice to see, but not required)

==============
Implementation:
Program will ask user to search books with different keys and numbers as many times as he wants.
User could request books from his library, sorted request result and transfer to csv.

==============
Description:
class Lib:
json_lib - dic{search_key: list_search_results_in_json}
addBooks() - update json_lib  with new pair search_key:list_search_results_in_json
getBooksByKey() - return one list by key from json_lib
getAllBooks() - return all lists from json_lib, pack in one list

api_request.py:
make api_request, return list of json data

Helpers:
def jsonToCSV(csv_path, list) - write json list to csv
def do_sort(list,header) - return sorted list, has dic { simplified_header, real_header}
def userInput - work with console
def do_csv (I used https://github.com/vinay20045/json-to-csv/blob/master/json_to_csv.py)
'''''


import csv
import api_request
'''
This class stores, update and retrive books data
'''
class Lib:
    def __init__(self):
        self.json_lib = {}
    def addBooks(self,key,list_json ):
        self.json_lib[key] = list_json.copy()
    def getBooksByKey(self,key):
        return self.json_lib[key]
    def getAllBooks(self):
        return get_lists_from_dic(self.json_lib)
#end class Lib

#helpers
def get_lists_from_dic(dic):
    res = []
    for key, value in dic.items():
        if type(value) is list:
            res.extend(value)
    return res

def to_string(s):
    try:
        return str(s)
    except:
        return s.encode('utf-8')

def reduce_item(key, value, res):
    # Reduction Condition 1
    # global res
    if type(value) is list:
        i = 0
        for sub_item in value:
            reduce_item(key + '_' + to_string(i), sub_item, res)
            i = i + 1
    # Reduction Condition 2
    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item(key + '_' + to_string(sub_key), value[sub_key], res)
    # Base Condition
    else:
        res[to_string(key)] = to_string(value)


def do_csv(date_list, csv_path, sort_by):
    data = []
    header = []
    for item in date_list:
        res = {}
        reduce_item("", item, res)
        header += res.keys()
        data.append(res.copy())

    header = list(set(header))
    header.sort()

    with open(csv_path, 'w') as f:
        writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        data_sorted = do_sort(data, sort_by)
        for row in data_sorted:
            writer.writerow(row)
    print("Just completed writing csv file with %d columns" % len(header))

def do_sort(list_to_sort, sort_key):
    sortBy = {"country": "_accessInfo_country", "price": "_saleInfo_listPrice_amount",
              "averageRating": "_volumeInfo_averageRating",
              "rating count": "_volumeInfo_ratingsCount", "published date": "_volumeInfo_publishedDate",
              "pageCount": "_volumeInfo_pageCount", "id":"_id"}

    newlist = sorted(list_to_sort, key=lambda k: k[sortBy[sort_key]])
    return  newlist


def flow1():
    lib = Lib()
    var = 1
    while True:
        var = input("Please enter 1-Get from Google lib, 2-Sort and get csv, 3-exit")
        print("you entered", var)
        if var == '1':
            find = input("Input search criteria:")
            print("looking for : ", find)
            num = input("Input how many results to get:")
            print("will get : ", num, " results")
            lib.addBooks(find, api_request.getBooks(find,num))
        elif var == '2':
            sort = input("Input sort criteria(example: price, averageRating, pageCount, id):")
            fileName = input("Input csv file_path:")
            all_or_key = input("Dd you want all (type 'all')or by key(type  key, Example: 'cat')")
            if(all_or_key == "all"):
                books = lib.getAllBooks()
            else:
                books = lib.getBooksByKey(all_or_key)
            do_csv(books,  fileName, "id")
        elif var == '3':
            break

flow1()

#debug
def flow2():
    key = 'kaka'
    lib = Lib()
    mydic = {}
    mydic = api_request.getBooks(key,'2')
    lib.addBooks(key, mydic )
    key = 'papa'
    mydic1 = api_request.getBooks(key,'2')
    lib.addBooks(key, mydic1)
    one_list = lib.getBooksByKey(key)
    all = lib.getAllBooks()
    do_csv(all,"c://temp/66.csv", "id")

#flow2()