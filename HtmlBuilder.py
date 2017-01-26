import json
import Library

jsonString=open('json/test.json').read()
outputFile=open('output/test.json', 'w')

# messy, but w/e, this should be encapsulated somewhere else as some sort of util.  It will probably come in handy
'''
Note that json brings back the string with ' instead of ", we have to make this conversion every time to walk along it
'''
def buildHtml():
    jsonLoad=json.loads(jsonString)
    keys=Library.getIdsFromJsonString(jsonString)
    print(keys)
    
    #check for attr, if not attr, set up a tag
    
    print(jsonLoad["html"])
    outputFile.write("")
    jsonString2 = str(jsonLoad["html"]).replace("'", '"')
    jsonLoad=json.loads(jsonString2)
    print(jsonLoad["p"])
    

buildHtml()
'''
#output file
open('output/helloWorld.html', 'w')

jsonString=open('json/helloWorld.json').read()
topLevelIdList=Library.getIdsFromJsonString(jsonString)
jsonLoads=json.loads(jsonString)

def buildHtml():
    #read json for initial ids
    parser = MyHtmlParser.HtmlIdParser()
    file = open('html/helloWorld.html')
    parser.feed(file.read())
'''    
'''
#Parse all of the json information into a dictionary


print(Library.getIdsFromJsonString(jsonString))


'''