import Tag

childTagList=[]
childerTagList=[]
attrDict= {}
attrDict['id']='foo'
attrDict['class']='bar'
childerTag=Tag.Tag("p", None, None, "testContent")
childerTagList.append(childerTag)

childTag=Tag.Tag("div", childerTagList, attrDict, None)
childTagList.append(childTag)

parentTag=Tag.Tag("html", childTagList, None, None)

print(parentTag.toXml())



#JsonIdHeirarchyParser.buildHtml()



#print(keyList)
#

#if(len(sys.argv) > 1):
#    args=sys.argv
#else:
#    args=['Main.py','default1', 'default2', 'default3']

#file=open("html/helloWorld.html", 'r')
#print(file.read())



