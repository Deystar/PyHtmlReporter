'''
Created on Jan 27, 2017

@author: cwitt
'''
class Tag(object):
    tagName=''
    childTagList=[]
    attributes={}
        
    def __init__(self, tagName, childTagList, attributes):
        self.tagName=tagName
        self.childTagList= childTagList
        self.attributes= attributes
    
    def setTagName(self, tagName):
        self.tagName=tagName
        
    def getTagName(self):
        return self.tagName
    
    def setChildTagList(self, childTagList):
        self.childTagList=childTagList
        
    def appendChildTagList(self, childTag):
        self.childTagList.append(childTag)
        
    def getChildTagList(self):
        return self.childTagList
    
    def setAttributes(self, attributes):
        self.attributes=attributes
        
    def addNewAttribute(self, key, value):
        self.attributes[key]=value
        
    def getAttributesString(self):
        attributesString=' '
        if self.attributes:
            for attribute in self.attributes.keys():
                if attribute is not None:
                    attributesString=attributesString + attribute + '="' + str(self.attributes[attribute]) + '" '
        return attributesString
    
    def getChildDataAsHtml(self):
        childTagListString=''
        if (self.childTagList) and (not self.childTagList is None):
            for childTag in self.childTagList:
                if type(childTag) is not None:
                    childTagListString=childTagListString + childTag.toHtml()
        return childTagListString
            
    def toHtml(self):
        attributesString= self.getAttributesString()
        childTagListString= self.getChildDataAsHtml()
        return "<" + self.tagName + attributesString + ">" + childTagListString + "</" + self.tagName + ">"

childTagList=[]
childerTagList=[]
attrDict= {}
attrDict['id']='foo'
attrDict['class']='bar'
childerTag=Tag("p", None, None)
childerTagList.append(childerTag)

childTag=Tag("div", childerTagList, attrDict)
childTagList.append(childTag)

parentTag=Tag("html", childTagList, None)

print(parentTag.toHtml())

    
    