'''

Main class, used for running from both IDE and terminal.

@author: cwitt
'''
from JsonIdHeirarchyParser import transformJsonIntoHeirarchy
from HtmlConstructor import HtmlConstructor
import sys

'''
This sets up the parameters that are used to supply the program with context.

jsonPath - Path to json that maps out the information that is going to be put into the html.
htmlPath - Path to the html that provides the structure for the new html page.
outputPath - Path where the new html will go.
'''
if(len(sys.argv)==1):
    jsonPath='json/example1.json'
    htmlPath='html/example1.html'
    outputPath='output/example1.html'
elif(len(sys.argv)==4):
    jsonPath=sys.argv[1]
    htmlPath=sys.argv[2]
    outputPath=sys.argv[3]
else:
    print("Incorrect arguments given.  Arguments are [python Main.py <pathToJsonFile> <pathToHtmlFile> <outputPath>]")

#Pulls the json out of the file and turns it into a JsonHeirarchy object.
jsonString=open(jsonPath).read()
heirarchyData=transformJsonIntoHeirarchy(jsonString)

#Pulls the html out of the file and feeds the data back into it, resulting in a fully formed html file.
htmlString=open(htmlPath).read()
constructor=HtmlConstructor(htmlString, heirarchyData, outputPath)
constructor.construct()
