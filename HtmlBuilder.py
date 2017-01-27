import json
import Library

jsonString=open('json/test.json').read()
outputFile=open('output/test.json', 'w')

# messy, but w/e, this should be encapsulated somewhere else as some sort of util.  It will probably come in handy
'''
Note that json brings back the string with ' instead of ", we have to make this conversion every time to walk along it
'''

def convertJsonLoadToString(jsonLoad):
    jsonString = str(jsonLoad).replace("'", '"')
    return jsonString

def makeTag(jsonLoad):
    attrsString=' '
    tagString='<'
    for key in jsonLoad.keys():
        if key == 'attrs':
            newJsonString=convertJsonLoadToString(jsonLoad["attrs"])
            attrsLoad=json.loads(newJsonString)
            for attr in attrsLoad.keys():
                attrsString=attrsString + attr + '="' + attrsLoad[attr]+'"'
        else:
            tagString=tagString+key
    return tagString+attrsString+'>'
    
    
def buildHtml():
    jsonLoad=json.loads(jsonString)
    keys=Library.getIdsFromJsonString(jsonString)
    print(keys)
    
    #check for attrs, if not attrs, set up a tag
    print(makeTag(jsonLoad["html"]))
    
    '''
    print(jsonLoad["html"])
    outputFile.write("")
    jsonString2 = convertJsonLoadToString(jsonLoad["html"])
    jsonLoad=json.loads(jsonString2)
    print(jsonLoad["p"])
    '''

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