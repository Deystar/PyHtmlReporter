'''
Created on Jan 25, 2017

@author: cwitt
'''
import json

jsonString=open('json/helloWorld.json').read()
print(json.loads(jsonString)["id2"])