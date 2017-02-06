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
    
    def setJsonHeirarchies(self, JsonHeirarchies):
        self.JsonHeirarchies=JsonHeirarchies
    
    def addToChildJsonHeirarchies(self, newJsonHeirarchy):
        self.childJsonHeirarchies.append(newJsonHeirarchy)
    
    def getJsonHeirarchies(self):
        return self.JsonHeirarchies()
    
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
    def getChildDataAsString(self):
        print("called childData")
        childJsonHeirarchiesString = ''
        if not self.childJsonHeirarchies is None:
            for child in self.childJsonHeirarchies:
                print("child len:" +str(len(self.childJsonHeirarchies)))
                print("child id: " +child.getIdAttr())
                print("child type: " +str(type(child)))
                
                childJsonHeirarchiesString=childJsonHeirarchiesString +child.toString()
                print("do i get here")
        return childJsonHeirarchiesString
    

    '''
'''
bottom=JsonIdHeirarchy("bottomId", None)

mid2=JsonIdHeirarchy("midId2", None)
midChildList=[]
midChildList.append(mid2)
mid=JsonIdHeirarchy("midId", midChildList)

childList=[]
childList.append(bottom)
childList.append(mid)
top=JsonIdHeirarchy("topId", [])
top.addToChildJsonHeirarchies(bottom)
top.addToChildJsonHeirarchies(mid)
print(top.toString())
'''
