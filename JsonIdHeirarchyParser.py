import json
from JsonIdHeirarchy import JsonIdHeirarchy

# messy, but w/e, this should be encapsulated somewhere else as some sort of util.  It will probably come in handy
'''
Note that json brings back the string with ' instead of ", we have to make this conversion every time to walk along it
'''
def __convertJsonLoadToString(jsonLoad):
    jsonString = str(jsonLoad).replace("'", '"')
    return jsonString

def __isLoadADictionary(jsonLoad):
    return type(jsonLoad)==dict
    
def transformJsonIntoHeirarchy(jsonString):
    jsonLoad=json.loads(jsonString)
    return __separateHeirarchyFromLoad(jsonLoad, None)
    
def getJsonHeirarchyFromListByName(jsonIdHeirarchyList, desiredName):
    for item in jsonIdHeirarchyList:
        if item.getIdAttr() == desiredName:
            return item
    return None
    
def __separateHeirarchyFromLoad(jsonLoad, jsonObject):
    if (jsonObject==None) :
        jsonObject=JsonIdHeirarchy("firstHierarchy", childJsonHeirarchies=[])
    for key in jsonLoad.keys():
        thisJsonObject = JsonIdHeirarchy(key, childJsonHeirarchies=[])
        
        if __isLoadADictionary(jsonLoad[key]):
            jsonString = __convertJsonLoadToString(jsonLoad[key])
            thisJsonLoad = json.loads(jsonString)
            jsonObject.addToChildJsonHeirarchies(thisJsonObject)
            __separateHeirarchyFromLoad(thisJsonLoad, thisJsonObject)
        else:
            thisJsonObject.setContent(jsonLoad[key])
            jsonObject.addToChildJsonHeirarchies(thisJsonObject)
    return jsonObject

'''
jsonLoad=json.loads(jsonString)
finalJsonLoad= __separateHeirarchyFromLoad(jsonLoad, None)

print("final: " + finalJsonLoad.toString())
for child in finalJsonLoad.childJsonHeirarchies:
    print(child.toString())
    for child2 in child.childJsonHeirarchies:
        print("child2 :" + child2.toString())
        print("child2 content :" + child2.getContent())
'''

'''  
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
    finishedTags=[]
    outOfTags=False
    
    while not outOfTags:
        for key in jsonLoad.keys():
            if key != 'attrs':
                print(makeTag(jsonLoad))
                finishedTags.append(key)
                jsonLoad=jsonLoad[key]
                print(jsonLoad)
        if not jsonLoad:
            outOfTags=True
    
    for tag in finishedTags:
        print("<"+tag+"/>")
    
    print(finishedTags)
'''