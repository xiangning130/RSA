
#coding: utf-8
import base64
import sys

text = open(sys.argv[1]).read()
#print text
text1=base64.b64decode(text).encode('hex')
text2=int(text1,16)
print(text2)

print "success"

