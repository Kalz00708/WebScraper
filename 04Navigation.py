'''
There are four types objects inside beautifulsoup
1. BeautifulSoup objects
    see 02
2. Tag objects
    retrieved in lists or individually by calling find and findAll on BeautifulSoup object
    you can access attributes of the tag object by
    - myTag.attrs       this will return a Python dictionary object
    - myTag.attrs[key]
3. NavigableString objects
    Used to represent text within tags
    can convert to unicode string by unicode(...)
    - If a tag has only one child and that child is a navigableString, you can get it by .string
    - If a tag has more than one thing you can iterate by
        1. strings
        2. stripped_strings     remove the whitespace inside the strings
4. The Comment object
    Used to find HTML comments in comment tags

Navigating Trees
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
.contents   get a list
.children   you can iterate over a tags directly children
.descendants    you can iterate all children

siblings: they are direct children of a same tag, and have same indentation level
.next_sibling/.previous_sibling     only one, and in real document it may be a string containing whitespace
.next_siblings/.previous_siblings

.parent     get direct parent
.parents    get all parents
'''
