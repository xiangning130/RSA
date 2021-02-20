#coding: utf-8
import base64
import sys

text = open(sys.argv[1]).read()
#print text
jarFile = open(sys.argv[2],"wb+")
jarFile.write(base64.b64decode(text).encode('hex'))
jarFile.close()
print "success"