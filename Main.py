import sys
import json

#Parse all of the json information into a dictionary
jsonString=open('json/helloWorld.json').read()

def getKeysFromAllDictionariesInJson(jsonString):
    initialJsonDictionary=json.loads(jsonString)
    print(initialJsonDictionary["ids"])
    isinstance(initialJsonDictionary["ids"], dict)
    finalIdList=[]
    newKeyDict={}
    outOfKeys=False
    firstIteration=True
    while not outOfKeys:
        for key in initialJsonDictionary.keys():
            if not firstIteration:
                initialJsonDictionary=newKeyDict
                print(key)
            if(isinstance(initialJsonDictionary[key], dict)):
                for thisKey in initialJsonDictionary[key].keys():
                    newKeyDict[thisKey]=initialJsonDictionary[thisKey]
                    finalIdList.append(key)
            else:
                finalIdList.append(key)
            if not newKeyDict:
                outOfKeys=True
            firstIteration=False
    return finalIdList


print(getKeysFromAllDictionariesInJson(jsonString))
'''    
while tempKeyList:
    tempKeyList = getKeysFromAllDictionariesInJson(tempKeyList)
print("done")
'''
'''
print(type(jsonDictionary[key]))
print(type(dict()))
print(type(jsonDictionary[key])==type(dict))
print(tempKeyList)
'''
#print(keyList)
#

#if(len(sys.argv) > 1):
#    args=sys.argv
#else:
#    args=['Main.py','default1', 'default2', 'default3']

#file=open("html/helloWorld.html", 'r')
#print(file.read())



