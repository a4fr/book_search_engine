# book_search_engine
python class for using http://it-ebooks.info API to download free best relevant books.

Properties
----------
- ``tags``
    A list of tags for find books
- ``limit_in_pages``
    Max number of deeping in search result. Every page has maximum 10 books. so if you wnat to see maximum 25 books suggestion, set ``limit_in_pages``  3.
    
    ``limit_in_pages = 0`` means there is no limit in find books and ``find`` methode proccess first to end results page.
- ``total_result``
    show you how many books in http://it-ebooks.info with this ``tags``.

Methodes
--------
- ``set_tag(tag_name)``
    add ``tag_name`` to ``tags`` list. This feature need for search book in online source

- ``find(sort_with="R", offline_json="")``
    Find best books and sort them for you. This methode can search online or use older JSON file (older online search).

    @sort_with    [R]elevant, [Y]ear, [A]uthor, [B]Publisher [P]age
        * it can be lower case or UPPER
        * -R -Y -A -P -B "reverse-sort"

    @offline_json    PATH of json file

    @return        list

    **Notice:** after online search, data store in JSON format in  like ``books-php-[31from187].json``, so you can use again this file for offline search.





 
