Python3 class for work with http://it-ebooks.info API to download best relevant books free.


Classes
-------
- ``search_engine``

    Main class for work with API.

Properties
----------
- ``tags``

    A list of tags for find books

- ``limit_in_pages``

    Max number of deeping in search result. Every page has maximum 10 books. so if you wnat to see maximum 30 books suggestion, set ``limit_in_pages``  3.
    
    ``limit_in_pages = 0`` means there is no limit in find books and ``find`` methode proccess first to end results page.

- ``total_result``

    show you how many books in http://it-ebooks.info with this ``tags``.


- `show_progressbar`

    Show progressbar in search online when you run app in shell. The default value is `False`.

Methodes
--------
- ``set_tag(tag_name)``

    add ``tag_name`` to ``tags`` list. This feature need for search book in online source

- ``find(sort_with="R", offline_json="")``

    Find best books and sort them for you. This methode can search online or use older JSON file (older online search).

    **@sort_with**

        * [R]elevant, [Y]ear, [A]uthor, [B]Publisher, [P]age

        * It can be lower case or UPPER

        * -R -Y -A -P -B "reverse-sort"

    **@offline_json**    PATH of json file

    **@return**        list

    **Notice:** after online search, data store in JSON format in  like ``books-php-[31from187].json``, so you can use again this file for offline search.




============
Sample codes
============
    >>> from search_engine import search_engine

    >>> felfeli = search_engine()

    >>> felfeli.set_tag("php")

    >>> felfeli.set_tag("mysql")

    >>> felfeli.limit_in_pages = 1

    >>> felfeli.show_progressbar = True

    >>> result = felfeli.find('p')

    >>> result = felfeli.find('-p') #reverse-sort

    >>> type(result)

    <class 'list'>

    >>> result = felfeli.find('b', "books-php-mysql-[10from138].json")

    >>> type(result)

    <class 'list'>

    >>> import pprint
    
    >>> pp = pprint.PrettyPrinter(indent=4)
    
    >>> pp.pprint(result[0])
    
    {   'Author': 'Armando Padilla , Tim Hawkins',
        'Description': 'This book contains tips, tricks, and techniques to make '
                       'new and existing PHP applications much faster and less '
                       'resource-hungry.\n'
                       '\n'
                       'Pro PHP Application Performance will help you understand '
                       'all the technologies and components which play a role in '
                       'how well your applications run. When seconds can mean '
                       'the difference between retaining a user and losing a '
                       "user, it's important for all of us to have optimization "
                       'as part of our project roadmap. But what components '
                       'within your application should you analyze? How should '
                       'you optimize? And how can you measure how well your '
                       'application is performing? These are some of the '
                       'questions that are answered in this book.\n'
                       '\n'
                       'Along the way you will also learn the &quot;why&quot; of '
                       'optimizing. You’ll discover why you should optimize a '
                       'specific component, why selecting one function over '
                       'another is beneficial, and how to find and use the '
                       'optimization tools available to the open source '
                       'community. You’ll also learn how to deploy caching '
                       'software as well as web server software.',

        'Download': 'http://filepi.com/i/sTM94d9',

        'ID': 427318464,

        'ISBN': 9781430228981,

        'Image': 'http://s.it-ebooks-api.info/6/pro_php_application_performance.jpg',

        'Page': 264,

        'Publisher': 'Apress',

        'SubTitle': 'Tuning PHP Web Projects for Maximum Performance',

        'Title': 'Pro PHP Application Performance',

        'Year': 2010,

        'isbn': '9781430228981'}
    



 
