#!/usr/bin/env python3

class Book:

    def __init__(self,title:str, page_count):
        self.title = title
        self._page_count = page_count


    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self,value):
        if value != int:
            print("page_count must be an integer")
        else:
            self._page_count = value
        

    pass
    
