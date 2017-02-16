'''
Created on Feb 7, 2017

Takes results from JsonIdHeirarchy and sets them in the html where the Json indicates by id.

@author: cwitt
'''
from bs4 import BeautifulSoup

class HtmlConstructor():
    jsonHeirarchy=None
    htmlString=''
    soup=None
    outputFile=None
    
    def __init__(self, htmlString, jsonIdHeirarchy, outputPath):
        self.jsonHeirarchy=jsonIdHeirarchy
        self.htmlString=htmlString
        self.soup=BeautifulSoup(self.htmlString, 'html.parser')
        self.outputFile=open(outputPath, 'w')
    
    #Finds the part of the soup object that deals with the desired tag
    def getSoupFromId(self, desiredId):
        return self.soup.find(id=desiredId)
    
    #Sets the data in the html and writes it to the new file
    def construct(self, jsonHeirarchies=None, heirarchyPathList=[]):
        self.getHeirarchyContent(jsonHeirarchies, heirarchyPathList)
        self.outputFile.write(BeautifulSoup.prettify(self.soup))
    
    
    def getHeirarchyContent(self, jsonHeirarchies, heirarchyPathList):
        # If no heirarchy is specified, use the one set in the class
        if jsonHeirarchies is None:
            jsonHeirarchies=self.jsonHeirarchy
            
        #check each of the children of the heirarchy
        for child in jsonHeirarchies.getChildJsonHeirarchies():
            
            #If there is no id by the child id, then skip the process
            if not self.getSoupFromId(child.getIdAttr()) is None:
                
                #If the child has children, move further down
                if len(child.getChildJsonHeirarchies()) > 0:
                    heirarchyPathList.append(child.getIdAttr())
                    self.getHeirarchyContent(child, heirarchyPathList)
                    
                #If the child has no children, set the content
                else:
                    heirarchyPathList.append(child.getIdAttr())
                    self.setContentInHtml(heirarchyPathList, child.getContent())
                    
                heirarchyPathList.remove(child.getIdAttr())
        
    def isResultStr(self, result):
        return isinstance(result, str)
    
    def isResultList(self, result):
        return isinstance(result, list)
    
    def setContentInHtml(self, heirarchyPathList, content, thisSoup=None):
        if thisSoup is None:
            thisSoup=self.soup
        for thisId in heirarchyPathList:
            thisSoup=thisSoup.find(id=thisId)
        
        if self.isResultStr(content):
            thisSoup.string=content
            
        if self.isResultList(content):
            self.handleListContent(thisSoup, content)
                
    def handleListContent(self, soup, content):
        contentString=''
        olTag=self.soup.new_tag('ol')
        soup.insert(0,olTag)
        for item in content:
            newTag=self.soup.new_tag('li')
            olTag.insert(1,newTag)
            contentString=''
            contentString=contentString + item
            newTag.string=contentString