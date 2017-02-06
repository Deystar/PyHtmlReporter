'''
Created on Jan 25, 2017

@author: cwitt
'''
from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        print("{tag:" + tag )
        if attrs:
            print("attr : {")
            for attr in attrs:
                print("     attr:", attr)
                print("{"+attr[0] + " : " + attr[1]+"}")
            
                    
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
        
    def handle_data(self, data):
        print("Encountered some data  :", data)

