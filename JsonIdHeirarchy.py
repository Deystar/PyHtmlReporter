'''
Created on Jan 27, 2017

@author: cwitt
'''
class JsonIdHeirarchy(object):
    idAttr=''
    childJsonHeirarchies=[]
    
    def __init__(self, idAttr, childJsonHeirarchies):
        self.idAttr= idAttr
        self.childJsonHeirarchies= childJsonHeirarchies
    
    def setIdAttr(self, idAttr):
        self.idAttr=idAttr
    
    def getIdAttr(self):
        return self.id
    
    def setJsonHeirarchies(self, JsonHeirarchies):
        self.JsonHeirarchies=JsonHeirarchies
    
    def addToJsonHeirarchies(self, newJsonHeirarchy):
        self.childJsonHeirarchies.append(newJsonHeirarchy)
    
    def getJsonHeirarchies(self):
        return self.JsonHeirarchies()
    
    def toString(self):
        childJsonHeirarchiesString=''
        childJsonHeirarchiesString=childJsonHeirarchiesString+"["
        if not self.childJsonHeirarchies is None:
            for child in self.childJsonHeirarchies:
                childJsonHeirarchiesString=childJsonHeirarchiesString + child.toString();
        childJsonHeirarchiesString=childJsonHeirarchiesString+"] "
        return self.idAttr + " > " + childJsonHeirarchiesString

'''
bottom=JsonIdHeirarchy("bottomId", None)

mid2=JsonIdHeirarchy("midId2", None)
midChildList=[]
midChildList.append(mid2)
mid=JsonIdHeirarchy("midId", midChildList)

childList=[]
childList.append(bottom)
childList.append(mid)
top=JsonIdHeirarchy("topId", childList)
print(top.toString())
'''