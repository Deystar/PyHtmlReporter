from JsonIdHeirarchyParser import transformJsonIntoHeirarchy
from MyHtmlParser import MyHtmlParser

jsonString=open('json/test.json').read()
heirarchyData=transformJsonIntoHeirarchy(jsonString)

htmlString=open('html/helloWorld.html').read()
parser = MyHtmlParser()
parser.feed(htmlString)

