import json
import Library
from JsonIdHeirarchy import JsonIdHeirarchy
from test.pickletester import MyList

jsonString=open('json/test.json').read()
outputFile=open('output/test.json', 'w')

# messy, but w/e, this should be encapsulated somewhere else as some sort of util.  It will probably come in handy
'''
Note that json brings back the string with ' instead of ", we have to make this conversion every time to walk along it
'''

def convertJsonLoadToString(jsonLoad):
    jsonString = str(jsonLoad).replace("'", '"')
    return jsonString

def isLoadADictionary(jsonLoad):
    return type(jsonLoad)==dict
    
def transformJsonIntoHeirarchy(jsonString):
    primaryJsonLoad=json.loads(jsonString)
    topHeirarchy=JsonIdHeirarchy("topHeirarchy", childJsonHeirarchies=[])
    outOfTags=False
    
    for key in primaryJsonLoad.keys():
        firstJsonObject=JsonIdHeirarchy(key, childJsonHeirarchies=[])
        topHeirarchy.addToJsonHeirarchies(firstJsonObject)
        jsonString=convertJsonLoadToString(primaryJsonLoad[key])
        jsonLoad=json.loads(jsonString)
        
        #Could just set up a dict with the parent and child names, then afterwards, create the objects
        #Dunno if objects are necessary with this logic
        counter=0
        #while 
            
            
        
    print(topHeirarchy.toString())
    
def separateHeirarchyFromLoad(jsonLoad, key):
    newJsonObject=JsonIdHeirarchy(key, childJsonHeirarchies=[])
    
'''
EEEEEEEHHHHHHHHHHHHHHHHHHH??????

I mean, it SHOULD append in order, just have to make multiples of this logic such that 

{'1': [2, 3], 2 : [3]} maybe, then infer that 1 > 2 > 3

'''
myList=[]
myDict={}
myDict["1"]=myList
myList.append(1)
myList.append(2)
print(myDict)

#transformJsonIntoHeirarchy(jsonString)
#transformJsonIntoHeirarchy(jsonString)
#print(isLoadADictionary(json.loads('{"armor":{"helmet":"hat","arms":"gauntlets"},"weapon":"sword"}')["armor"]))
#print(isLoadADictionary(json.loads('{"helmet": "hat"}')["helmet"]))
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