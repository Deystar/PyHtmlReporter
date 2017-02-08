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
    
    def __init__(self, htmlString, jsonIdHeirarchy):
        self.jsonHeirarchy=jsonIdHeirarchy
        self.htmlString=htmlString
        self.soup=BeautifulSoup(self.htmlString, 'html.parser')
    
    def getSoupFromId(self, desiredId):
        return self.soup.find(id=desiredId)
    
    def getHeirarchyContent(self, jsonHeirarchies=None, heirarchyPath=None):
        # If no heirarchy is specified, use the one set in the class
        if jsonHeirarchies is None:
            jsonHeirarchies=self.jsonHeirarchy
            
        if heirarchyPath is None:
                heirarchyPath=self.jsonHeirarchy.getIdAttr()
        
        #check each of the children of the heirarchy
        for child in jsonHeirarchies.getChildJsonHeirarchies():
            
            #If there is no id by the child id, then skip the process
            if not self.getSoupFromId(child.getIdAttr()) is None:
                
                #If the child has children, move further down
                if len(child.getChildJsonHeirarchies()) > 0:
                    thisHeirarchyPath= heirarchyPath + " > " + child.getIdAttr()
                    self.getHeirarchyContent(child, thisHeirarchyPath)
                    
                #If the child has no children, set the content
                else:
                    print(child.getContent())
                    finalPath=heirarchyPath + " > " + child.getIdAttr()
                    print("path: " + finalPath)
    
    def isResultStr(self, result):
        return result is str
    
    def isResultList(self, result):
        return result is list

'''
jsonString=open('html/helloWorld.html').read()
soup=BeautifulSoup(jsonString,'html.parser')

result=soup.find(id="armor")

result2=result.find(id="helmet")
result2.string="hat"

print(soup.prettify())
'''
