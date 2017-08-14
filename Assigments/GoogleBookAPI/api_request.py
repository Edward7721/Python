
import requests



def doRequst(key,num):
    r = requests.request('GET', 'https://www.googleapis.com/books/v1/volumes?q=' + key + '&maxResults=' + num)
    return r

def getJSON(responce):
    mdic = responce.json()
    return mdic

def getBooks(find,num):
    res= getJSON(doRequst(find,num))
    return res["items"]

def getStatusCode(key,num):
    r =  doRequst(key,num)
    return r.status_code

#getBooks("cat")

