import json
import urllib.request
from operator import itemgetter #uses in sorting data

"""
    find best book that you need and return them
    @author    Ali Najafi (mail.ali.najafi@gmail.com)
    @source    http://it-ebooks-api.info/
"""
from oneconf.utils import save_json_file_update

class search_engine:
    def __init__(self):
        self.tags = []
        self.limit_in_pages = 0 # value <= 0 means there is no limit
        self.total_result = 0
        self.all_pages = 0
    
    
    """
        this feature need for search book in online source
    """
    def set_tag(self, tag_name):
        self.tags.append(str(tag_name))
    
    
    """
        @return dict
    """
    def request(self, url):
        r = urllib.request.urlopen(url).read().decode('utf8')
        r = json.loads(r)
        return r
    
    
    def get_books__detail_from_source(self):
        finded_books = []
        tags = ''
        if len(self.tags) > 0:
            for tag in self.tags:
                tags += " " + tag
            tags = tags.strip()
        else:
            raise('length of "tags" is ZERO. function needs tags to search')
        #request pages
        START_PAGE = 1
        END_PAGE = 1
        CURRENT_PAGE = START_PAGE
        while CURRENT_PAGE <= END_PAGE:
            url = 'http://it-ebooks-api.info/v1/search/'+tags+'/page/'+str(CURRENT_PAGE)
            request = self.request(url)
            if CURRENT_PAGE == 1:
                self.total_result = request["Total"]
                self.all_pages = int(request['Total']) // 10 + 1
                #prepare END_PAGE
                if (self.limit_in_pages > 0) and (self.all_pages > self.limit_in_pages):
                    END_PAGE = self.limit_in_pages
                else:
                    END_PAGE = self.all_pages
            #append new books
            finded_books.extend(request["Books"])
            CURRENT_PAGE += 1
        #extract other detail of books
        for book_index in range(len(finded_books)):
            url = "http://it-ebooks-api.info/v1/book/"+str(finded_books[book_index]["ID"])
            other_details = self.request(url)
            for detail in other_details:
                if detail not in {"Error", "Time"}:
                    if detail in {"Year", "ISBN", "isbn", "Page"}:
                        #need this for sorting
                        finded_books[book_index][detail] = int(other_details[detail])
                    else:
                        finded_books[book_index][detail] = other_details[detail]
        #save data as json file
        name = 'books-%s-[%sfrom%s].json' % (tags.replace(" ", "-"), len(finded_books), self.total_result)
        save_json_file_update(name, finded_books)
        print('"%s" Saved!' % name)
        return finded_books
    
    
    """
        load json file data instance of online source
        @return list
    """
    def get_books_detail_from_json_file(self, PATH):
        if PATH:
            file = open(PATH, 'r')
            return json.loads(file.read())
    
    
    """
        find best books and sort them for you
        @sort_with    [R]elevant, [Y]ear, [A]uthor, [B]Publisher, [P]age
            * it can be lower case or UPPER
            * -R -Y -A -P -B "reverse-sort"
        @offline_json    PATH of json file
        @return        list
    """
    def find(self, sort_with="R", offline_json=""):
        sort_mod = {'r': 'Relevant',
                    'y': 'Year',
                    'a': 'Author',
                    'b': 'Publisher',
                    'p': 'Page'}
        #check sort_with
        sort_with = sort_with.strip()
        sort_with = sort_with.lower()
        reverse = False
        if len(sort_with) > 2:
            raise('"sort_with" Error')
        elif len(sort_with) == 2 and sort_with[0] == '-':
            reverse = True
            sort_with = sort_with[1]
        elif len(sort_with) == 1 and sort_with in sort_mod.keys():
            pass
        else:
            raise('"sort_with" Error')
        #check offline mod
        if not offline_json:
            data = self.get_books__detail_from_source()
        else:
            data = self.get_books_detail_from_json_file(offline_json)
        #sorting
        if sort_with == 'r':
            if  reverse == True:
                data.reverse()
        else:
            data = sorted(data, key=itemgetter(sort_mod[sort_with]), reverse=reverse)
        
        return data
        
    
    
    """
        save json (dict) data to a file
        @input data must be dict()
    """
    def save_json_to_file(self, PATH, data):
        file = open(str(PATH), 'w')
        file.write(json.dumps(data, indent=4, separators=(',', ': ')))
        file.close()
    
    
