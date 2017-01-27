'''
Created on Jan 27, 2017

@author: cwitt
'''
class Tag(object):
    tagName=''
    childTagList=[]
    attributes={}
    content=''
        
    def __init__(self, tagName, childTagList, attributes, content):
        self.tagName=tagName
        self.childTagList= childTagList
        self.attributes= attributes
        self.content= content
    
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
                    childTagListString=childTagListString + childTag.toXml()
        return childTagListString
    
    def setContent(self, content):
        self.content= content
        
    def getContent(self):
        if not self.content is None:
            return self.content
        else: 
            return ''
            
    def toXml(self):
        attributesString= self.getAttributesString()
        childTagListString= self.getChildDataAsHtml()
        return "<" + self.tagName + attributesString + ">" + self.getContent() + childTagListString + "</" + self.tagName + ">"
    


    
    