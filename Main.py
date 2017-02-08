from JsonIdHeirarchyParser import transformJsonIntoHeirarchy
from HtmlConstructor import HtmlConstructor

jsonString=open('json/test.json').read()
heirarchyData=transformJsonIntoHeirarchy(jsonString)
print(heirarchyData.toString())

htmlString=open('html/helloWorld.html').read()
constructor=HtmlConstructor(htmlString, heirarchyData)
constructor.getHeirarchyContent()