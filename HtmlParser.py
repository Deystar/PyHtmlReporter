'''
Created on Jan 25, 2017

@author: cwitt
'''
import MyHtmlParser

# instantiate the parser and fed it some HTML
parser = MyHtmlParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')