#! /usr/bin/python3.4

import pprint
from search_engine import search_engine

felfeli = search_engine()
felfeli.set_tag("html")
felfeli.set_tag("css")
felfeli.limit_in_pages = 2
felfeli.show_progressbar = True
result = felfeli.find('-y')
#result = felfeli.find('-b', "books-html-css-[180from176].json")

data = []
for book in result:
    tmp = dict()
    tmp['Title'] = book['Title']
    tmp['Page'] = book['Page']
    tmp['Publisher'] = book['Publisher']
    tmp['Year'] = book['Year']
    data.append(tmp)
    
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
