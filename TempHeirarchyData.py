from JsonIdHeirarchyParser import transformJsonIntoHeirarchy
from JsonIdHeirarchy import JsonIdHeirarchy

def initializeHeirarchyData(jsonPath):
    jsonString=open('json/test.json').read()
    heirarchyData=transformJsonIntoHeirarchy(jsonString)
    return heirarchyData
