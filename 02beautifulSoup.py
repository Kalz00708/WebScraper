import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

for i in range(1, len(sys.argv)):
    try:
        html = urlopen(sys.argv[i])
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        '''
        There is an issue which the content on the page not quite being what we expected
        bsObj.nonExistingTag is None
        bsObj.nonExistingTag.someTag will raise an exception AttributeError
        '''
        bsObj = BeautifulSoup(html.read(), "html.parser")
        try:
            '''
            The document is https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
            
            Here are some basic points
            the other way is to use findAll or find
            .tegName <--> find() <--> findAll(limit = 1)
            find("h2") <--> findAll("h2")[0]

            findAll(name, attrs, recursive, text, limit, **kwargs)
            - name: tag name
            - attrs: tag attributes
            - recursice: True means also find in their children, False means not
            - text: content
            - limit: the max size of the return list
            - **kwargs: you can use attr={'class': fliter} <--> class=fliter

            fliter types
            - string: find the value same with this string
            - list: find the value same with one of element inside the list
            - regular expression: find the value follpw the r.e, usage re.compile()
                ?=  read the next character and judge if equal but not move to that
                ?!  read the next character and judge if not equal but not move to that
                ?:  non-capturing group
            - lambda expression: format     lambda parameter: body
                e.g. lambda tag:len(tag.attrs) == 2
            - function: find the value follow the function
                def has_class_but_no_id(tag):
                        return tag.has_attr('class') and not tag.has_attr('id')
            - True: return without restrictions
            '''
            badContent1 = bsObj.nonExistingTag
            badContent2 = bsObj.nonExistingTag.anotherTag
        except AttributeError:
            print("badContent2: Tag was not found")
        else:
            print(badContent2)
        finally:
            if badContent1 == None:
                print("badContent1: Tag was not found")
            else:
                print(badContent1)
