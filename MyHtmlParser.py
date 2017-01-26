'''
Created on Jan 25, 2017

@author: cwitt
'''
import Library
import HtmlBuilder
from html.parser import HTMLParser

startTagcounter=0

class HtmlIdParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        startTagcounter+1
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
