'''
Created on Jan 27, 2017

@author: cwitt
'''
class JsonIdHeirarchy(object):
    idAttr=''
    childJsonHeirarchies=[]
    content=''
    
    def __init__(self, idAttr, childJsonHeirarchies):
        self.idAttr= idAttr
        self.childJsonHeirarchies= childJsonHeirarchies
    
    def setIdAttr(self, idAttr):
        self.idAttr=idAttr
    
    def getIdAttr(self):
        return self.idAttr
    
    def setContent(self, content):
        self.content=content
    
    def getContent(self):
        return self.content
    
    def setChildJsonHeirarchies(self, childJsonHeirarchies):
        self.childJsonHeirarchies=childJsonHeirarchies
    
    def addToChildJsonHeirarchies(self, newJsonHeirarchy):
        self.childJsonHeirarchies.append(newJsonHeirarchy)
    
    def getChildJsonHeirarchies(self):
        return self.childJsonHeirarchies
    
    #Workaround for recursion issue
    def getChildDataAsString(self):
        childJsonHeirarchiesString = ''
        if not self.childJsonHeirarchies is None:
            for child in self.childJsonHeirarchies:
                childJsonHeirarchiesString=childJsonHeirarchiesString +child.getIdAttr() + " "
        return childJsonHeirarchiesString
    
    def toString(self):
        childJsonHeirarchiesString=''
        childJsonHeirarchiesString=childJsonHeirarchiesString+"["
        
        childJsonHeirarchiesString=childJsonHeirarchiesString + self.getChildDataAsString()
        childJsonHeirarchiesString=childJsonHeirarchiesString+"] "
        return self.idAttr + " > " + childJsonHeirarchiesString
    
    
'''    
bottom=JsonIdHeirarchy("bottomId", [])

mid2=JsonIdHeirarchy("midId2", [])
midChildList=[]
midChildList.append(mid2)
mid=JsonIdHeirarchy("midId", midChildList)

childList=[]
childList.append(bottom)
childList.append(mid)
top=JsonIdHeirarchy("topId", childList)

print(top.toString())
'''