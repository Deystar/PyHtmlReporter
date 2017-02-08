from JsonIdHeirarchyParser import transformJsonIntoHeirarchy
from HtmlConstructor import HtmlConstructor

jsonString=open('json/example1.json').read()
heirarchyData=transformJsonIntoHeirarchy(jsonString)

htmlString=open('html/example1.html').read()
constructor=HtmlConstructor(htmlString, heirarchyData, 'output/example1.html')
constructor.construct()