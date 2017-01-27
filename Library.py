import json
'''
#Returns all ids in json - note: doesn't quite work, might be unneccessary

def getKeysFromAllDictionariesInJson(jsonString):
    initialJsonDictionary=json.loads(jsonString)
    finalIdList=[]
    newKeyDict={}
    outOfKeys=False
    while not outOfKeys:
        for key in initialJsonDictionary.keys():
            if(isinstance(initialJsonDictionary[key], dict)):
                for thisKey in initialJsonDictionary[key].keys():
                    newKeyDict[thisKey]=initialJsonDictionary[key][thisKey]
                    finalIdList.append(key)
            else:
                finalIdList.append(key)
        if not newKeyDict:
            outOfKeys=True
        else:
            initialJsonDictionary.clear()
            initialJsonDictionary.update(newKeyDict)
            newKeyDict.clear()
    return finalIdList
'''

def getIdsFromJsonString(jsonString):
    initialJsonDictionary=json.loads(jsonString)
    finalKeyList=[]
    for key in initialJsonDictionary.keys():
        finalKeyList.append(key)
    return finalKeyList
'''
def getValueFromJson(jsonString):
    myString=JsonIdHeirarchyParser.jsonString
    json
'''