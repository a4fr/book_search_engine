#! /usr/bin/python3.4

import pprint
from search_engine import search_engine

felfeli = search_engine()
felfeli.set_tag("python")
felfeli.limit_in_pages = 1
#result = felfeli.find('-p')
result = felfeli.find('b', "books-php-[10from138].json")

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
